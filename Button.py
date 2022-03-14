import pygame
import pygame.font
from settings import settings

class Button():
    def __init__(self,screen,msg) -> None:
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.width=100
        self.height=100
        self.button_color=(0,0,0)
        self.text_color=(50,50,250)
        self.font=pygame.font.SysFont(None,32)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.prep_msg(msg)
    def prep_msg(self,msg):
        self.msg_img=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_img_rect=self.msg_img.get_rect()
        self.msg_img_rect.center=self.screen_rect.center
    def draw(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)

