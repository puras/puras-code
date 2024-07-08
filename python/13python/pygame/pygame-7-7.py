import pygame as pg

pg.init()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption('城堡保卫战')

keys = [False, False, False, False]
hero_pos = [100, 100]
hero_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\dude.png')

running = True
while running:
    screen.fill(0)
    screen.blit(hero_img, hero_pos)

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
