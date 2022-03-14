# from turtle import screensize
# import pygame
from settings import settings
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen) -> None:
        super().__init__()
        self.image=pygame.image.load("alien_ship.png")
        self.screen=screen
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.moving_left=True
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self,aliens):
        collided = any(self.rect.colliderect(alien.rect)for alien in aliens if self != alien)
        if collided:
            self.moving_left=not self.moving_left
        self.rect.y+=settings.alien_velocity
        if self.rect.x<settings.alien_spacing:
            self.moving_left=False
        elif self.rect.x>settings.screen_width-settings.alien_spacing:
            self.moving_left=True
        if self.moving_left:
            self.rect.x-=settings.alien_velocity
        else:
            self.rect.x+=settings.alien_velocity
