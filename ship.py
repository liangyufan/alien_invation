import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        #self.lives = settings.ship_lives
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")

        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self, settings):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= settings.ship_speed
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)