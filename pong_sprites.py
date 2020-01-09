import pygame
from config import *


class PlankSprites(pygame.sprite.Sprite):
    """平板精灵"""
    def __init__(self, vel=0):
        super().__init__()
        self.image = pygame.image.load("./plank.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, Setting.PLANK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = Setting.SCREEN_RECT.centerx
        self.rect.bottom = Setting.SCREEN_RECT.bottom - 10
        self.vel = vel
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.vel
        if self.rect.right >= Setting.SCREEN_RECT.right:
            self.rect.right = Setting.SCREEN_RECT.right
        if self.rect.x <= 0:
            self.rect.x = 0


class Ball(pygame.sprite.Sprite):
    """球精灵"""
    def __init__(self, x_vel=0, y_vel=0):
        super().__init__()
        self.image = pygame.image.load("./ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, Setting.BALL_SIZE)
        self.rect = self.image.get_rect()
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y -= self.y_vel

        if self.rect.x <= 0 or self.rect.right >= Setting.SCREEN_RECT.right:
            self.x_vel = -self.x_vel
        if self.rect.y <= 0:
            self.y_vel = -self.y_vel
        if self.rect.y >= Setting.SCREEN_RECT.bottom:
            self.kill()


class Brick(pygame.sprite.Sprite):
    """砖块精灵"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./brick.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, Setting.BRICK_SIZE)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Text(object):
    """文字块"""
    def __init__(self, text, size=24):
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", size)
        self.text = self.font.render(text, True, Setting.WHITE)
        self.rect = self.text.get_rect()
        self.rect.centerx = Setting.SCREEN_RECT.centerx
        self.rect.y = 10
