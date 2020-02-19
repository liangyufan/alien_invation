import sys
import pygame

from ship import Ship
from settings import Settings
import tools

def screen_update(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw(screen)
    ship.blitme()
    pygame.display.flip()

def bullets_update(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = pygame.sprite.Group()

    while True:
        tools.event_handler(settings, ship, bullets)

        ship.update(settings)
        bullets_update(bullets)

        screen_update(settings, screen, ship, bullets)

run_game()