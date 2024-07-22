import math

import pygame as pg

pg.init()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption('城堡保卫战')

# 跟踪箭头变量
arrows = []

keys = [False, False, False, False]
hero_pos = [100, 100]
hero_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\dude.png')

grass_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\grass.png')
castle_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\castle.png')

# 加载箭头
arrow_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\bullet.png')
# 加载獾
badguy_img1 = pg.image.load('resources/images/badguy.png')
badguy_img = badguy_img1

running = True
while running:
    screen.fill(0)
    for i in range(int(width / grass_img.get_width() + 1)):
        for j in range(int(height / grass_img.get_height() + 1)):
            screen.blit(grass_img, (i * 100, j * 100))

    screen.blit(castle_img, (0, 20))
    screen.blit(castle_img, (0, 110 + 20))
    screen.blit(castle_img, (0, 110 * 2 + 20))
    screen.blit(castle_img, (0, 110 * 3 + 20))
    # screen.blit(hero_img, hero_pos)
    pos = pg.mouse.get_pos()
    angle = math.atan2(pos[1] - (hero_pos[1] + 32), pos[0] - (hero_pos[0] + 26))
    hero_rot = pg.transform.rotate(hero_img, 360 - angle * 57.29)
    hero_pos1 = (hero_pos[0] - hero_rot.get_rect().width / 2,
                 hero_pos[1] - hero_rot.get_rect().height / 2)
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

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                keys[0] = True
            elif event.key == pg.K_s:
                keys[2] = True
            elif event.key == pg.K_a:
                keys[1] = True
            elif event.key == pg.K_d:
                keys[3] = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                keys[0] = False
            elif event.key == pg.K_s:
                keys[2] = False
            elif event.key == pg.K_a:
                keys[1] = False
            elif event.key == pg.K_d:
                keys[3] = False
        # 当玩家点击鼠标，就要射出一支箭
        # 这段代码会检查是否鼠标被点击了
        # 如果点击了就会得到鼠标的位置并根据玩家的和光标的位置计算出箭头旋转角度
        # 旋转角度的值存放在Arrows这个数组里
        if event.type == pg.MOUSEBUTTONDOWN:
                    # shoot.play()
                    pos = pg.mouse.get_pos()
                    # acc[1] += 1
                    arrows.append([math.atan2(pos[1] - (hero_pos1[1] + 32),
                                              pos[0] - (hero_pos1[0] + 26)),
                                   hero_pos1[0] + 32, hero_pos1[1] + 26])

    if keys[0]:
        hero_pos[1] -= 1
    elif keys[2]:
        hero_pos[1] += 1
    if keys[1]:
        hero_pos[0] -= 1
    elif keys[3]:
        hero_pos[0] += 1

    pg.display.flip()

pg.quit()
