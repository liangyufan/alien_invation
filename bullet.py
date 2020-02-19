import pygame
from pygame.sprite import Sprite
from pygame import Rect

class Bullet(Sprite):
    def __init__(self, settings, ship):
        super().__init__()
        self.rect = Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)