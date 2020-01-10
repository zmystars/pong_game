import pygame


class Setting(object):
    SCREEN_RECT = pygame.Rect(0, 0, 800, 600)
    FRAME_PER_SEC = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PLANK_SIZE = (200, 10)
    BALL_SIZE = (50, 50)
    BRICK_SCALE = (10, 10)
    BRICK_SIZE = (int((SCREEN_RECT.width - 200) / BRICK_SCALE[0]), 15)

