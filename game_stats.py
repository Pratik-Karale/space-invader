from settings import settings as st
class gameStats():
    def __init__(self) -> None:
        # self.reset()
        self.game_active=False
        self.reset=False
        self.score=0
    def reset_stats(self):
        self.game_active=True
        self.score=0
        self.reset=False

game_stats=gameStats()