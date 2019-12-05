import pygame

SCREEN_RECT = pygame.Rect(0, 0, 800, 600)
FRAME_PER_SEC = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLANK_SIZE = (200, 10)
BALL_SIZE = (50, 50)
BRICK_SCALE = (10, 10)
BRICK_SIZE = (int(SCREEN_RECT.width / BRICK_SCALE[0]), 15)


class PlankSprites(pygame.sprite.Sprite):
    """平板精灵"""
    def __init__(self, vel=0):
        super().__init__()
        self.image = pygame.image.load("./plank.png")
        self.image = pygame.transform.scale(self.image, PLANK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 10
        self.vel = vel

    def update(self):
        self.rect.x += self.vel
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.x <= 0:
            self.rect.x = 0


class Ball(pygame.sprite.Sprite):
    """球精灵"""
    def __init__(self, x_vel=0, y_vel=0):
        super().__init__()
        self.image = pygame.image.load("./ball.png")
        self.image = pygame.transform.scale(self.image, BALL_SIZE)
        self.rect = self.image.get_rect()
        self.x_vel = x_vel
        self.y_vel = y_vel

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y -= self.y_vel

        if self.rect.x <= 0 or self.rect.right >= SCREEN_RECT.right:
            self.x_vel = -self.x_vel
        if self.rect.y <= 0:
            self.y_vel = -self.y_vel
        if self.rect.y >= SCREEN_RECT.bottom:
            self.kill()


class Brick(pygame.sprite.Sprite):
    """砖块精灵"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./brick.png")
        self.image = pygame.transform.scale(self.image, BRICK_SIZE)
        self.rect = self.image.get_rect()


class Text(object):
    """文字块"""
    def __init__(self, text, size=24):
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", size)
        self.text = self.font.render(text, True, WHITE)
        self.rect = self.text.get_rect()
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = 10
