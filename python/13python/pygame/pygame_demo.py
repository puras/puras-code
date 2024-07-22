from time import sleep

import pygame as pg
import random

pg.init()
pg.mixer.music.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\audio\\moonlight.wav')
pg.mixer.music.play(-1, 0.0)
pg.mixer.music.set_volume(0.25)

a_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\healthbar.png')
b_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\health.png')
shoot = pg.mixer.Sound('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\audio\\shoot.wav')
shoot.set_volume(0.2)

screen = pg.display.set_mode((800, 600))
h = 194

while True:
    screen.fill((255, 255, 255))

    screen.blit(a_img, (5, 5))
    for i in range(h):
        screen.blit(b_img, (i + 8, 8))
    sleep(1)
    h -= random.randint(5, 50)

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            shoot.play()