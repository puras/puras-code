import math

import pygame as pg

pg.init()

width, height = 640, 480

screen = pg.display.set_mode((width, height))
pg.display.set_caption('城堡保卫战')

# 2
hero_pos = [100, 100]
hero_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\dude.png')

# 1
grass_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\grass.png')
castle_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\castle.png')
#         w      a     s       d
keys = [False, False, False, False]

running = True
while running:
    screen.fill(0)

    #1
    for i in range(int(width / grass_img.get_width() + 1)):
        for j in range(int(height / grass_img.get_height() + 1)):
            screen.blit(grass_img, (i * 100, j * 100))

    screen.blit(castle_img, (0, 15))
    screen.blit(castle_img, (0, 115 + 15))
    screen.blit(castle_img, (0, 115 * 2 + 15))
    screen.blit(castle_img, (0, 115 * 3 + 15))

    # screen.blit(hero_img, hero_pos)
    # 2
    pos = pg.mouse.get_pos()
    angle = math.atan2(pos[1] - hero_pos[1] + 32, pos[0] - hero_pos[0] + 26)
    hero_rot = pg.transform.rotate(hero_img, 360 - angle * 57.29)
    hero_pos1 = (hero_pos[0] - hero_rot.get_rect().width / 2,
                 hero_pos[1] - hero_rot.get_rect().height / 2)
    screen.blit(hero_rot, hero_pos1)

    # 2
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
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