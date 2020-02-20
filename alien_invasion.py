import sys
import pygame

from ship import Ship
from alien import Alien
from settings import Settings
import tools

def screen_update(settings, screen, ship, bullets, aliens):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw(screen)
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def bullets_update(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def aliens_init(screen, alien):
    aliens = pygame.sprite.Group()
    screen_rect = screen.get_rect()
    n_x = int((screen_rect.width - alien.rect.width) / (2 * alien.rect.width))
    n_y = int((screen_rect.height - 6 * alien.rect.height) / (2 * alien.rect.height))
    for y in range(n_y):
        for x in range(n_x):
            aliens.add(Alien(screen, x, y))
    return aliens

def aliens_update(aliens, settings):
    for alien in aliens.sprites():
        if alien.rect.right >= alien.screen_rect.right or alien.rect.left <= 0:
            for alien in aliens.sprites():
                alien.y += settings.alien_y_speed
            settings.alien_dir *= -1
            break
    aliens.update(settings)

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = pygame.sprite.Group()
    alien = Alien(screen, 0, 0)
    aliens = aliens_init(screen, alien)

    while True:
        tools.event_handler(settings, ship, bullets)

        ship.update(settings)
        bullets_update(bullets)
        aliens_update(aliens, settings)

        screen_update(settings, screen, ship, bullets, aliens)

run_game()