import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    ship=Ship(screen,pygame)
    pygame.display.set_caption("ALIEN INVASION")
    while True:
        screen.fill(settings.bg_color)
        ship.blit_me()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        pygame.display.flip()

run_game()
    
