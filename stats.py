class Stats:
    def __init__(self, settings):
        self.game_active = False

        self.reset(settings)

    def reset(self, settings):
        self.score = 0
        self.score_per_alien = 10
        self.ship_lives = settings.ship_lives