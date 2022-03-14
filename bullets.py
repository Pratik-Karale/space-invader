# from email.mime import image
import pygame
from pygame.sprite import Sprite
from settings import settings as st

class Bullet(Sprite):
    def __init__(self,screen,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(
            ship.rect.centerx-st.bullet_width
            ,ship.rect.y,
            st.bullet_width,
            st.bullet_height
        )
        self.rect.centerx=ship.rect.centerx
        self.color=st.bullet_color
        self.velocity=st.bullet_velocity
    def move(self):
        self.rect.y-=self.velocity
    def update(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


