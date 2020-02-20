import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def __keydown_handler(key, settings, ship, bullets):
    if key == pygame.K_q:
        sys.exit()
    if key == pygame.K_RIGHT:
        ship.moving_right = True
    if key == pygame.K_LEFT:
        ship.moving_left = True
    if key == pygame.K_SPACE:
        if len(bullets) < settings.bullet_limit:
            bullets.add(Bullet(settings, ship))

def __keyup_handler(key, ship):
    if key == pygame.K_RIGHT:
        ship.moving_right = False
    if key == pygame.K_LEFT:
        ship.moving_left = False

def __mousebuttondown_handler(pos, settings, screen, ship, aliens, bullets, button_start, stats):
    if button_start.rect.collidepoint(pos):
        ship.lives = settings.ship_lives
        reset(screen, aliens, bullets)
        stats.game_active = True

def event_handler(settings, screen, aliens, ship, bullets, button_start, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            __keydown_handler(event.key, settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            __keyup_handler(event.key, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            __mousebuttondown_handler(event.pos, settings, screen, ship, aliens, bullets, button_start, stats)

def screen_update(settings, screen, ship, bullets, aliens, stats, button_start):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw(screen)
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        button_start.draw()
    pygame.display.flip()

def bullets_update(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def aliens_init(screen, aliens):
    alien = Alien(screen, 0, 0)
    n_x = int((alien.screen_rect.width - alien.rect.width) / (2 * alien.rect.width))
    n_y = int((alien.screen_rect.height - 6 * alien.rect.height) / (2 * alien.rect.height))
    for y in range(n_y):
        for x in range(n_x):
            aliens.add(Alien(screen, x, y))
    del alien

def aliens_update(aliens, settings):
    for alien in aliens.sprites():
        if alien.rect.right >= alien.screen_rect.right or alien.rect.left <= 0:
            for alien in aliens.sprites():
                alien.y += settings.alien_y_speed
            settings.alien_dir *= -1
            break
    aliens.update(settings)

def __ship_hit(ship, aliens):
    if pygame.sprite.spritecollideany(ship, aliens):
        return True
    for alien in aliens.sprites():
        if alien.rect.bottom >= ship.screen_rect.bottom:
            return True
    return False

def reset(screen, aliens, bullets):
    bullets.empty()
    aliens.empty()
    sleep(0.5)
    aliens_init(screen, aliens)

def go(screen, ship, bullets, aliens, stats):
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        reset(screen, aliens, bullets)
    if __ship_hit(ship, aliens):
        ship.lives -= 1
        if ship.lives > 0:
            reset(screen, aliens, bullets)
        else:
            stats.game_active = False