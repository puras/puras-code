import pygame


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        pygame.init()

        # 1、创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2、创建游戏时钟
        # 3、调用私有方法，精灵和精灵组的创建
        # 4、设置定时事件 - 创建敌机 1s