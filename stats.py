class Stats:
    def __init__(self, settings):
        self.game_active = False
        self.high_score = 0

        self.reset(settings)

    def reset(self, settings):
        self.ship_lives = settings.ship_lives
        self.score = 0
        self.level = 1