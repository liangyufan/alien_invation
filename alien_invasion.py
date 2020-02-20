import sys
import pygame

from ship import Ship
from settings import Settings
from button import Button
from stats import Stats
from scoreboard import Scoreboard
import tools

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, settings)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    #tools.aliens_init(screen, aliens)
    stats = Stats(settings)
    button_start = Button(screen, "start")
    sb = Scoreboard(screen, settings, stats)

    while True:
        tools.event_handler(settings, screen, aliens, ship, bullets, button_start, stats)

        if stats.game_active:
            ship.update(settings)
            tools.bullets_update(bullets, aliens)
            tools.aliens_update(aliens, settings)
            tools.go(settings, screen, ship, bullets, aliens, stats)

        tools.screen_update(settings, screen, ship, bullets, aliens, stats, button_start, sb)

run_game()