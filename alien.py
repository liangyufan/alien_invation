import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + self.rect.width * 2 * x
        self.rect.y = self.rect.height + self.rect.height * 2 * y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, settings):
        self.x += settings.alien_x_speed * settings.alien_dir
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)