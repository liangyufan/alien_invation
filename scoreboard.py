import pygame

from ship import Ship

class Scoreboard:
    def __init__(self, screen, settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.font = pygame.font.SysFont(None, 48, True)
        self.text_color = (100, 100, 0)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        self.str_score = "{:,}".format(int(round(self.stats.score, -1)))
        self.score_image = self.font.render(self.str_score, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.str_high_score = "{:,}".format(int(round(self.stats.high_score, -1)))
        self.high_score_image = self.font.render(self.str_high_score, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.str_level = str(self.stats.level)
        self.level_image = self.font.render(self.str_level, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = 70

    def prep_ships(self):
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ship_lives):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        #self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)

        #self.prep_high_score()
        self.screen.blit(self.high_score_image, self.high_score_rect)

        self.screen.blit(self.level_image, self.level_rect)

        #self.prep_ships()
        self.ships.draw(self.screen)