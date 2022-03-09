import pygame

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("ALIEN INVASION")
    while True:
        screen.fill((0,0,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        pygame.display.flip()

run_game()
    
