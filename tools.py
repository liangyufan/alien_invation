import sys
import pygame

from bullet import Bullet

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

def event_handler(settings, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            __keydown_handler(event.key, settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            __keyup_handler(event.key, ship)