import math
import random

import pygame as pg

width, height = 640, 480
# keys用来记录按键情况：WASD（依次对应）
keys = [False, False, False, False]
# hero_pos表示玩家位置
hero_pos = [100, 100]

# 跟踪玩家的精度变量，记录射出的箭头数和被击中的獾的数量
# 之后我们会用到这些信息用来计算射击精确度
acc = [0, 0]
# 跟踪箭头变量
arrows = []
# 定义一个定时器，使游戏里经过一段时间后就新建一个敌人
bad_timer = 100
bad_timer1 = 0
badguys = [[640, 100]]
health_val = 194

pg.init()
screen = pg.display.set_mode((width, height))

# 加载图片
hero_img = pg.image.load('resources/images/dude.png')
# 背景和风景
grass_img = pg.image.load('resources/images/grass.png')
# 加载箭头
castle_img = pg.image.load('resources/images/castle.png')
arrow_img = pg.image.load('resources/images/bullet.png')
# 加载獾
badguy_img1 = pg.image.load('resources/images/badguy.png')
badguy_img = badguy_img1

running = True

while running:
    # 在给屏幕画任何东西之前用黑色进行填充
    screen.fill(0)

    # 用图片填充背景，图片大小100*100
    for x in range(width // grass_img.get_width() + 1):
        for y in range(height // grass_img.get_height() + 1):
            screen.blit(grass_img, (x * 100, y * 100))
    # 画上背景
    screen.blit(castle_img, (0, 30))
    screen.blit(castle_img, (0, 135))
    screen.blit(castle_img, (0, 240))
    screen.blit(castle_img, (0, 345))

    # 首先获取鼠标与英雄的位置，然后获取通过Atan2函数得出的角度和弧度
    # 当英雄被旋转时，它的位置将会改变
    # 所以需要计算英雄的新位置，然后将其在屏幕上显示出来
    pos = pg.mouse.get_pos()
    angle = math.atan2(pos[1] - (hero_pos[1] + 32), pos[0] - (hero_pos[0] + 26))
    hero_rot = pg.transform.rotate(hero_img, 360-angle*57.29)
    hero_pos1 = (hero_pos[0] - hero_rot.get_rect().width / 2, hero_pos[1] - hero_rot.get_rect().height / 2)
    screen.blit(hero_rot, hero_pos1)

    # 在屏幕上画箭头
    # vely和velx的值是根据三角定理算出来的
    # 10是箭头的速度，if表过式是检查箭头是否超出来屏幕范围
    # 如果超出，就删除这个箭头
    # 第二个for表过式是循环来把箭头根据相应的旋转画出来
    for bullet in arrows:
        idx = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(idx)

        idx += 1

        for projectile in arrows:
            a1 = pg.transform.rotate(arrow_img, 360 - projectile[0] * 57.29)
            screen.blit(a1, (projectile[1], projectile[2]))

    # 更新并显示坏蛋
    # 检查bad_timer是否为0，如果为0，创建一个獾，然后重新设置bad_timer
    # 第一个循环更新獾的X坐标，检查獾是否超出屏幕范围，如果超出，将獾删除
    # 第二个循环是来画出所有的獾
    if bad_timer == 0:
        badguys.append([640, random.randint(50, 430)])
        bad_timer = 100 - (bad_timer1 * 2)
        if bad_timer1 >= 35:
            bad_timer1 = 35
        else:
            bad_timer1 += 5
    index_badguy = 0
    for bad_guy in badguys:
        if bad_guy[0] < -64:
            badguys.pop(index_badguy)
        bad_guy[0] -= 1
        # 獾可以炸掉城堡
        # 如果獾的X坐标离左边小于64
        # 就删除獾，并减少游戏里的健康值，减少的大小为5到20里的随机数
        # 当然獾冲过来并且在碰到城堡时会消失
        bad_rect = pg.Rect(badguy_img.get_rect())
        bad_rect.top = bad_guy[1]
        bad_rect.left = bad_guy[0]
        if bad_rect.left < 64:
            health_val -= random.randint(5, 20)
            badguys.pop(index_badguy)
        index_badguy += 1
    for bad_guy in badguys:
        screen.blit(badguy_img, bad_guy)

    # 更新屏幕
    pg.display.flip()

    # 检查事件，如果有退出命令，则终止程序的执行
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # 根据按下的键来更新按键记录数组
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                keys[0] = True
            elif event.key == pg.K_a:
                keys[1] = True
            elif event.key == pg.K_s:
                keys[2] = True
            elif event.key == pg.K_d:
                keys[3] = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                keys[0] = False
            elif event.key == pg.K_a:
                keys[1] = False
            elif event.key == pg.K_s:
                keys[2] = False
            elif event.key == pg.K_d:
                keys[3] = False
        # 当玩家点击鼠标，就要射出一支箭
        # 这段代码会检查是否鼠标被点击了
        # 如果点击了就会得到鼠标的位置并根据玩家的和光标的位置计算出箭头旋转角度
        # 旋转角度的值存放在Arrows这个数组里
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(pos[1] - (hero_pos1[1] + 32), pos[0] - (hero_pos1[0] + 26)),
                           hero_pos1[0] + 32, hero_pos1[1] + 26])

    if keys[0]:
        hero_pos[1] -= 5
    elif keys[2]:
        hero_pos[1] += 5
    if keys[1]:
        hero_pos[0] -= 5
    elif keys[3]:
        hero_pos[0] += 5
    bad_timer -= 1

pg.quit()
exit()
