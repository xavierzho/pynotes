import copy
import random
import pygame


# 蛇的模型
snake_list = [[10, 10]]
# 500 X500 背景大小
# 食物的模型 随机生成
x = random.randint(10, 490)
y = random.randint(10, 490)
food_point = [x, y]

# 初始化小蛇方向
move_up = False
move_down = False
move_left = False
move_right = True
# 画布
# 初始化游戏组件
pygame.init()
# 设置画布大小
screen = pygame.display.set_mode((500, 500))
# 设置名字
title = pygame.display.set_caption("贪吃蛇游戏")
# 设置游戏时钟

clock = pygame.time.Clock()

while True:
    # 电影是 一帧一帧的 30FPS
    clock.tick(20)
    # 游戏循环
    # 背景填充为白色
    screen.fill([255, 255, 255])
    # 绘制圆圈点
    food_rect = []
    pygame.draw.circle(screen, [255, 0, 0], food_point, 15)
    """贪吃蛇移动 获取键盘事件"""
    for pos in snake_list:
        snake_pos = pygame.draw.circle(screen, [255, 0, 0], pos, 5)
    # 获取电脑的事件
    for event in pygame.event.get():
        # 获取键盘事件
        if event.type == pygame.KEYDOWN:
            # 向下移动
            if event.key == pygame.K_DOWN:
                move_up = False
                move_down = True
                move_left = False
                move_right = False
            if event.key == pygame.K_UP:
                move_up = True
                move_down = False
                move_left = False
                move_right = False

            if event.key == pygame.K_LEFT:
                move_up = False
                move_down = False
                move_left = True
                move_right = False
            if event.key == pygame.K_RIGHT:
                move_up = False
                move_down = False
                move_left = False
                move_right = True

    # 身子的移动
    snake_len = len(snake_list) - 1
    while snake_len > 0:
        snake_list[snake_len] = copy.deepcopy(snake_list[snake_len - 1])
        snake_len -= 1
    # 蛇头的移动
    if move_down:
        snake_list[snake_len][1] += 10
        if snake_list[snake_len][1] > 500:
            snake_list[snake_len][1] = 0

    if move_up:
        snake_list[snake_len][1] -= 10
        if snake_list[snake_len][1] > 500:
            snake_list[snake_len][1] = 0

    if move_left:
        snake_list[snake_len][0] -= 10
        if snake_list[snake_len][0] < 0:
            snake_list[snake_len][0] = 500

    if move_right:
        snake_list[snake_len][0] += 10
        if snake_list[snake_len][0] > 500:
            snake_list[snake_len][0] = 0
    # 绘制食物
    food_rect = pygame.draw.circle(screen, [255, 0, 0], food_point, 15)
    # 循环
    snake_rect = []
    for snake_pos in snake_list:
        snake_rect.append(pygame.draw.circle(screen, [255, 0, 0], snake_pos, 5))
    # Python解释器知道下方定义了一个函数
        # 如果食物与蛇发生碰撞，碰撞检测方法
        if food_rect.collidepoint(snake_pos):
            snake_list.append(food_point)
            # 重新生成食物
            food_point = [random.randint(10, 490), random.randint(10, 490)]
            break
    # 蛇吃到了自己应该结束游戏

    snake_head_rect = snake_rect[0]
    count = len(snake_rect)

    while count > 1:
        # 蛇头与身子任何一个点都有可能发生碰撞
        if snake_head_rect.colliderect(snake_rect[count-1]):
            print('吃到尾巴了，游戏结束')
            pygame.quit()
        count -= 1

    # 把绘制的东西显示出来
    pygame.display.update()
