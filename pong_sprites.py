import pygame

SCREEN_RECT = pygame.Rect(0, 0, 800, 600)
FRAME_PER_SEC = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class PlankSprites(pygame.sprite.Sprite):
    def __init__(self, vel=0):
        super().__init__()
        self.image = pygame.image.load("./plank.png")
        self.image = pygame.transform.scale(self.image, (200, 10))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 30
        self.vel = vel

    def update(self):
        self.rect.x += self.vel
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.x <= 0:
            self.rect.x = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self, x_vel=0, y_vel=0):
        super().__init__()
        self.image = pygame.image.load("./ball.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.x_vel = x_vel
        self.y_vel = y_vel

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.x <= 0 or self.rect.right >= SCREEN_RECT.right:
            self.x_vel = -self.x_vel
        if self.rect.y <= 0:
            self.y_vel = -self.y_vel
        if self.rect.y >= SCREEN_RECT.bottom:
            self.kill()


class Text(object):
    def __init__(self, text):
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", 24)
        self.text = self.font.render(text, True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = SCREEN_RECT.centerx
        self.text_rect.y = 10
