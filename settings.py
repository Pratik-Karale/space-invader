class Settings():
    def __init__(self):
        self.screen_width=500
        self.screen_height=500
        self.bg_color=(0,0,255)

        # ships
        self.total_ships=3

        # ship
        self.ship_velocity=4

        # bullet
        self.bullet_velocity=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=255,255,255
        self.max_bullets=10

        # alien
        self.alien_width=50
        self.alien_height=50
        self.alien_spacing=self.alien_width/4
        self.alien_velocity=1
        self.aliens_score=50
        self.aliens_multiplier=1.5

        # 
        self.speed_multiplier=1.1
    def reset(self):
        self.total_ships=3
        self.ship_velocity=4
        self.bullet_velocity=1
        self.bullet_width=3
        self.bullet_height=15
        self.max_bullets=10
        self.alien_width=50
        self.alien_height=50
        self.alien_spacing=self.alien_width/4
        self.alien_velocity=1

settings=Settings()