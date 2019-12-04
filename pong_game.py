import pygame
from pong_sprites import *


class PongGame(object):
    def __init__(self):
        print("游戏初始化...")
        self.keep_going = True
        self.lives = 3
        self.points = 0
        self.speed_x = 5
        self.speed_y = 5
        self.score_board = None
        self.scores = None
        self.ball = None
        self.draw_string = ""

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.set_caption("PongGame")
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        self.plank = PlankSprites()
        self.plank_group = pygame.sprite.Group(self.plank)
        
        self.ball_group = pygame.sprite.Group()
        
    def __create_a_ball(self):
        self.ball = Ball(self.speed_x, self.speed_y)
        self.ball_group.add(self.ball)

    def start_game(self):
        print("游戏开始...")
        while self.keep_going:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            if self.lives > 0 and len(self.ball_group) == 0:
                self.__create_a_ball()
                self.lives -= 1
            elif self.lives == 0 and len(self.ball_group) == 0:
                self.__one_game_finished()
            else:
                self.__show_score_board()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PongGame.game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.__create_a_ball()
                    self.lives = 3
                    self.points = 0

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.plank.vel = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.plank.vel = -5
        else:
            self.plank.vel = 0

    def __check_collide(self):
        catch = pygame.sprite.spritecollide(self.plank, self.ball_group, False)
        if len(catch) > 0:
            self.ball.y_vel = -self.ball.y_vel
            self.points += 1

    def __update_sprites(self):
        self.screen.fill(BLACK)

        self.plank_group.update()
        self.plank_group.draw(self.screen)
        
        self.ball_group.update()
        self.ball_group.draw(self.screen)

        self.score_board = Text(self.draw_string)
        self.screen.blit(self.score_board.text, self.score_board.rect)

    def __show_score_board(self):
        self.draw_string = "Points:" + str(self.points) + " Lives:" + str(self.lives)

    def __one_game_finished(self):
        self.draw_string = "Game Over. Your scores was: " + str(self.points)
        self.draw_string += ". Press F1 to play again. "

    @staticmethod
    def game_over():
        print("游戏结束。")
        pygame.quit()
        exit()


def main():
    game = PongGame()
    game.start_game()


if __name__ == '__main__':
    main()
