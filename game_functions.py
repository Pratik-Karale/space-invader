from turtle import Screen
import pygame
from alien import Alien
from settings import settings
from bullets import Bullet
import time
from game_stats import game_stats

# from ship import Ship

def check_events(ship,bullets,screen,play_btn):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            handle_play_btn(play_btn,mouse_pos)

        elif event.type==pygame.KEYDOWN:
            handle_keydown(event,ship,bullets,screen)
        elif event.type==pygame.KEYUP:
            handle_keyup(event,ship)
def handle_play_btn(play_btn,mouse_pos):
    button_clicked=play_btn.rect.collidepoint(*mouse_pos)
    if button_clicked and not game_stats.game_active:
        pygame.mouse.set_visible(False)
        game_stats.game_active=True
        game_stats.reset=True


def handle_keydown(event,ship,bullets,screen):
    if event.key==pygame.K_RETURN and not game_stats.game_active:
        game_stats.game_active=True
    if event.key==pygame.K_LEFT and ship.can_move_left():
        ship.move_left()
        ship.moving_left=True
    elif event.key==pygame.K_RIGHT and ship.can_move_right():
        ship.move_right()
        ship.moving_right=True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<settings.max_bullets:
            bullet=Bullet(screen,ship)
            bullets.add(bullet)

def handle_keyup(event,ship):
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_RIGHT:
        ship.moving_right=False


def update_bullets(bullets,aliens,screen):
    del_old_bullets(bullets)
    for bullet in bullets.sprites():
        bullet.move()
    bullets.update()
    handle_shots(bullets,aliens)
    handle_empty_fleet(bullets,aliens,screen)

def handle_empty_fleet(bullets,aliens,screen):
    # print(len(aliens))
    if len(aliens)==0:
        bullets.empty()
        create_fleet(aliens,screen)
        settings.aliens_score*=settings.aliens_multiplier
        increase_speed()

def increase_speed():
    settings.ship_velocity*=settings.speed_multiplier
    settings.alien_velocity*=settings.speed_multiplier
    settings.bullet_velocity*=settings.speed_multiplier

def handle_shots(bullets,aliens):
    collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)
    if collisions!={}:
        game_stats.score+=settings.aliens_score
    if collisions!={} and len(aliens)==0:
        time.sleep(0.5)

def update_screen(screen,ship,bullets,aliens,play_button,sb):
    screen.fill(settings.bg_color)
    sb.show_score()
    if not game_stats.game_active:
        play_button.draw()
    else:
        update_bullets(bullets,aliens,screen)
        update_ship(ship,aliens,screen)
        update_fleet(aliens,screen)
    pygame.display.update()

def update_fleet(aliens,screen):
    aliens.draw(screen)
    for alien in aliens:
        if alien.rect.y>screen.get_rect().height:
            aliens.remove(alien)


def update_ship(ship,aliens,screen):
    ship.blit_me()
    if pygame.sprite.spritecollideany(ship,aliens):
        aliens.empty()
        create_fleet(aliens,screen)
        time.sleep(0.5)
        ship.center()
        settings.total_ships-=1
    if not settings.total_ships:
        game_stats.reset=True
        pygame.mouse.set_visible(True)

def del_old_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.bottom<0:
            bullets.remove(bullet)


def create_fleet(aliens,screen):
    ALIEN_COUNT=10
    current_x=0
    current_y=0
    for _ in range(ALIEN_COUNT):
        if current_x>=settings.screen_width:
            current_y+=settings.alien_height+settings.alien_spacing+50
            current_x=settings.alien_spacing*2
        alien=Alien(screen)
        current_x+=settings.alien_spacing
        alien.rect.x=current_x
        current_x+=settings.alien_spacing+alien.rect.width
        alien.rect.y=current_y
        aliens.add(alien)

def game_over(ship,*groups):
    ship.centerx=settings.screen_width/2
    for group in groups:
        group.empty()
    settings.reset()
    game_stats.game_active=False
