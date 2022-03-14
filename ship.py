import pygame
from settings import settings

class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("ship.png")
        # self.image=pygame.transform.scale(self.image)
        # self.image=py_obj.transform.scale(self.image.convert(),(50,50))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False


    def move_left(self):
        self.rect.x-=settings.ship_velocity
    def move_right(self):
        self.rect.x+=settings.ship_velocity
    def blit_me(self):
        self.screen.blit(self.image,self.rect)
    def can_move_left(self):
        return self.rect.x>0
    def can_move_right(self):
        return self.rect.x+50<settings.screen_width
    def center(self):
        self.rect.centerx=self.screen_rect.centerx
# screen.blit(pygame.image.load("ship.png"))
