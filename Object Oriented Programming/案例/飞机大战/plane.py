#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import time
from pygame.locals import *


# 抽象出来一个基类
class BasePlane(object):
    def __init__(self, screen, image_path):
        """
        初始化基类函数
        :param screen: 主窗体
        :param image_path: 加载的图片
        """
        self.x = 150
        self.y = 450
        self.screen = screen
        self.image_path = pygame.image.load(image_path)
        self.bullet_list = []  # 存储所有的子弹

    def display(self):
        self.screen.blit(self.image_path, (self.x, self.y))
        # 完善子弹的展示逻辑
        need_del_item_list = []
        for item in self.bullet_list:
            if item.judge():
                need_del_item_list.append(item)
        # 重新遍历
        for i in need_del_item_list:
            self.bullet_list.remove(i)
            pass

        for bullet in self.bullet_list:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让子弹移动，下次再显示就会看到修改后的位置
        pass

    pass


class CommonBullet(object):
    """
    公共子弹类
    """

    def __init__(self, x, y, screen, bullet_type):
        self.type = bullet_type
        self.screen = screen
        if self.type == 'player':
            self.x += 13
            self.y = y - 20
            self.image_path = 'bullet2.png'
        elif self.type == 'enemy':
            self.x = x
            self.y = y + 10
            self.image_path = 'bullet.png'
        self.image = pygame.image.load(self.image_path)

    def move(self):
        """
        子弹移动
        :return:
        """
        if self.type == 'player':
            self.y -= 2
        elif self.type == 'enemy':
            self.y += 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y > 500 or self.y < 0:
            return True
        else:
            return False

    pass


# 创建飞机类
class PlayerPlane(BasePlane):
    def __init__(self, screen):
        """
        初始化函数
        :param screen: 主窗体对象
        """
        super().__init__(screen, 'player.png')  # 调用父类的构造方法
        # 设置player飞机默认位置

        pass

    def move_left(self):
        """
        左移动
        :return:
        """
        if self.x > 0:
            self.x -= 10

        pass

    def move_right(self):
        """
        右移动
        :return:
        """
        if self.x < 310:
            self.x += 10

        pass

    def move_up(self):
        if self.y > 460:
            self.y -= 10

    def move_down(self):
        if self.y < 0:
            self.y += 10

    # 发射子弹
    def shot_bullet(self):
        # 创建一个子弹对象
        new_bullet = CommonBullet(self.x, self.y, self.screen, 'player')
        self.bullet_list.append(new_bullet)
        pass

    pass


# 创建敌机类
class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, 'enemyplane.jpg')
        # 默认设置一个方向
        self.direction = 'right'
        self.screen = screen

        # 设置enemy飞机默认位置
        self.x = 0
        self.y = 0

    def shot_bullet(self):
        num = random.randint(1, 50)
        if num == 5:
            new_bullet = CommonBullet(self.x, self.y, self.screen, 'enemy')
            self.bullet_list.append(new_bullet)
        pass

    def move(self):
        # 随机移动
        if self.direction == 'right':
            self.x += 0.5
            pass
        elif self.direction == "left":
            self.x -= 0.5
        if self.x > 350 - 20:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
        pass

    pass


def key_control(player_obj):
    """
    键盘检测
    :param player_obj:
    :return:
    """

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            print('quit')
            exit()
            pass
        elif event.type == KEYDOWN:
            # 按键检测
            if event.type == K_a or event.type == K_LEFT:
                print('left')
                player_obj.move_left()
            elif event.type == K_d or event.type == K_RIGHT:
                print('right')
                player_obj.move_right()
            elif event.type == K_w or event.type == K_UP:
                print('up')
                player_obj.move_up()
            elif event.type == K_s or event.type == K_DOWN:
                print('down')
                player_obj.move_down()
            elif event.type == K_SPACE:
                print('space发射子弹')
                player_obj.shot_bullet()


def main():
    # 创建一个窗口对象，来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 设定一个背景图片对象
    background = pygame.image.load('background.png')
    # 设置一个title
    pygame.display.set_caption('阶段总结-飞机大战小游戏')
    # 设置背景音乐
    pygame.mixer.init()
    pygame.mixer_music.load('starSky.mp3')
    # 设置音量
    pygame.mixer.music.set_volume(0.2)
    # 循环次数-1表示无限循环
    pygame.mixer.music.play(-1)

    # 创建飞机对象
    player = PlayerPlane(screen)
    # 创建敌机对象
    enemy = EnemyPlane(screen)
    # 设定显示的内容
    while True:
        screen.blit(background, (0, 0))
        # 显示player飞机图片
        player.display()
        # 显示敌机图片
        enemy.display()
        enemy.move()  # 敌机移动
        enemy.shot_bullet()  # 敌机随机发送子弹
        # 获取键盘事件
        key_control(player)

        # 更新显示的内容
        pygame.display.update()
        pygame.time.Clock().tick(15)


if __name__ == '__main__':
    main()
