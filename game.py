import pygame
from alien import Alien
from score_board import ScoreBoard
from settings import settings
from ship import Ship
from bullets import Bullet
import game_functions as f
from pygame.sprite import Group
import time
from game_stats import game_stats
from Button import Button

lvl=1

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    ship=Ship(screen)
    pygame.display.set_caption("ALIEN INVASION")
    bullets=Group()
    aliens=Group()
    f.create_fleet(aliens,screen)
    sb=ScoreBoard(screen)
    play_button=Button(screen,"P L A Y")
    while (True):
        f.update_screen(screen,ship,bullets,aliens,play_button,sb)
        f.check_events(ship,bullets,screen,play_button)
        if not game_stats.game_active:
            continue
        time.sleep(0.02)
        if  ship.moving_left and ship.can_move_left():
            ship.move_left()
        elif  ship.moving_right and ship.can_move_right():
            ship.move_right()
        aliens.update(aliens)
        if not settings.total_ships:
            f.game_over(ship,aliens,bullets)


run_game()

