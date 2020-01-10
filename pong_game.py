import pygame
from config import *
from pong_sprites import *


class PongGame(object):
    def __init__(self):
        print("游戏初始化...")
        self.keep_going = True
        self.lives = 3
        self.points = 0
        self.score_board = None
        self.tips_board = None
        self.result_board = None
        self.ball = None
        self.draw_string = ""
        self.ball_have_vel = False
        self.pause = False

        self.screen = pygame.display.set_mode(Setting.SCREEN_RECT.size)
        pygame.display.set_caption("PongGame")
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        """初始化创建游戏精灵"""
        self.plank = PlankSprites()
        self.plank_group = pygame.sprite.Group(self.plank)

        self.ball_group = pygame.sprite.Group()

        self.brick_group = pygame.sprite.Group()

        # 排列砖块位置
        for i in range(Setting.BRICK_SCALE[0]):
            for j in range(Setting.BRICK_SCALE[1]):
                self.brick = Brick()
                self.brick.rect.x = i * Setting.BRICK_SIZE[0] + 100 + 2 * i
                self.brick.rect.y = j * Setting.BRICK_SIZE[1] + 80 + 2 * j
                self.brick_group.add(self.brick)

    def start_game(self):
        """游戏循环"""
        print("游戏开始...")
        while self.keep_going:
            self.clock.tick(Setting.FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__show_score_board()
            self.__show_tips()
            pygame.display.update()

            if self.pause is False:
                self.__update_sprites()
                if self.lives > 0 and len(self.ball_group) == 0:
                    self.ball = Ball()
                    self.ball_group.add(self.ball)
                    self.ball_have_vel = False
                    self.lives -= 1
                elif self.lives == 0 and len(self.ball_group) == 0:
                    self.__one_game_finished()

    def __event_handler(self):
        """事件检测"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PongGame.game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.__init__()
                if event.key == pygame.K_F2:
                    self.pause = not self.pause
                if event.key == pygame.K_SPACE and self.ball:
                    self.ball.x_vel += 5
                    self.ball.y_vel += 5
                    self.ball_have_vel = True

        if self.ball and not self.ball_have_vel:
            self.ball.rect.centerx = pygame.mouse.get_pos()[0]
            self.ball.rect.bottom = self.plank.rect.top - 10
        # 使用鼠标控制平板位置
        self.plank.rect.centerx = pygame.mouse.get_pos()[0]

        # 使用键盘控制平板位置
        """
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.plank.vel = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.plank.vel = -5
        else:
            self.plank.vel = 0
        """

    def __check_collide(self):
        """碰撞检测"""
        # 平板接球
        catch = pygame.sprite.spritecollide(self.plank, self.ball_group, False, pygame.sprite.collide_mask)
        if len(catch) > 0:
            self.ball.y_vel = -self.ball.y_vel

        # 球碰撞砖块
        if pygame.sprite.groupcollide(self.ball_group, self.brick_group, False, True, pygame.sprite.collide_mask):
            self.ball.y_vel = -self.ball.y_vel

    def __update_sprites(self):
        """更新显示"""
        self.screen.fill(Setting.BLACK)  # 清屏

        self.plank_group.update()
        self.plank_group.draw(self.screen)

        self.ball_group.update()
        self.ball_group.draw(self.screen)

        self.brick_group.update()
        self.brick_group.draw(self.screen)

    def __show_score_board(self):
        """绘制记分板"""
        self.points = Setting.BRICK_SCALE[0] * Setting.BRICK_SCALE[1] - len(self.brick_group)
        self.draw_string = "Points:" + str(self.points) + " Lives:" + str(self.lives)
        self.score_board = Text(self.draw_string)
        self.screen.blit(self.score_board.text, self.score_board.rect)

    def __show_tips(self):
        """显示提示信息"""
        if self.ball_have_vel is False:
            self.draw_string = "Press [Space] to start."
        elif self.ball_have_vel is True and self.pause is False:
            self.draw_string = "Press [F2] to pause."
        elif self.ball_have_vel is True and self.pause is True:
            self.draw_string = "Press [F2] to resume."
        self.tips_board = Text(self.draw_string)
        self.tips_board.rect.y = 34
        self.screen.blit(self.tips_board.text, self.tips_board.rect)

    def __one_game_finished(self):
        """一局游戏结束，显示得分"""
        self.points = Setting.BRICK_SCALE[0] * Setting.BRICK_SCALE[1] - len(self.brick_group)
        self.draw_string = "Game Over. Your scores was: " + str(self.points)
        self.draw_string += ". Press F1 to play again. "
        self.result_board = Text(self.draw_string, 30)
        self.result_board.rect.centery = Setting.SCREEN_RECT.centery
        self.screen.blit(self.result_board.text, self.result_board.rect)

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
