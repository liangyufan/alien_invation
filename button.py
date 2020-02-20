import pygame

class Button():
    def __init__(self, screen, msg):
        self.screen = screen
        self.width = 200
        self.height = 50
        self.bgcolor = (0, 0, 255)
        self.textcolor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = screen.get_rect().center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.textcolor, self.bgcolor)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.bgcolor, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)