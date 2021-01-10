#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import time
from pygame.locals import *


# 创建飞机类
class PlayerPlane(object):
    def __init__(self, screen):
        """
        初始化函数
        :param screen: 主窗体对象
        """
        # 设置player飞机默认位置
        self.x = 150
        self.y = 450
        # 设置要显示内容的窗口
        self.screen = screen
        # 载入飞机图片对象
        self.image_name = 'player.png'
        self.image = pygame.image.load(self.image_name)
        # 子弹列表
        self.bullet_list = []
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

    def display(self):
        """
        显示飞机
        :return:
        """
        self.screen.blit(self.image, (self.x, self.y))
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

    # 发射子弹
    def shot_bullet(self):
        # 创建一个子弹对象
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(new_bullet)
        pass

    pass


# 创建子弹类
class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 13
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load('bullet2.png')
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        pass

    def move(self):
        self.y -= 1
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y < 0:
            return True
        else:
            return False
        pass

    pass


# 敌机的子弹类
class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 13
        self.y = y + 10
        self.screen = screen
        self.image = pygame.image.load('bullet.png')
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        pass

    def move(self):
        self.y += 3
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y > 500:
            return True
        else:
            return False
        pass

    pass


# 创建敌机类
class EnemyPlane(object):
    def __init__(self, screen):
        # 默认设置一个方向
        self.direction = 'right'
        self.screen = screen
        self.bullet_list = []
        # 设置enemy飞机默认位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        # 载入飞机图片对象
        self.image_name = 'enemyplane.jpg'
        self.image = pygame.image.load(self.image_name)

    def display(self):
        # 显示敌机以及子弹位置的信息
        self.screen.blit(self.image, (self.x, self.y))
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

    def shot_bullet(self):
        num = random.randint(1, 50)
        if num == 5:
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)
        pass

    def move(self):
        # 随机移动
        if self.direction == 'right':
            self.x += 0.5
            pass
        elif self.direction == "left":
            self.x -= 0.5
        if self.x > 350-20:
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
