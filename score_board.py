from settings import settings
import pygame
from game_stats import game_stats
class ScoreBoard():
    def __init__(self,screen) -> None:
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=game_stats
        self.previous_score=self.stats.score
        self.text_color=(200,255,255)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()

    def prep_score(self):
        score_str=f"{int(self.stats.score)}"
        self.score_image=self.font.render(score_str,True,self.text_color,settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.y=20
        self.score_rect.x=self.screen_rect.width-self.score_rect.width-20
    
    def show_score(self):
        if self.previous_score<self.stats.score:
            self.prep_score()
        self.screen.blit(self.score_image,self.score_rect)
