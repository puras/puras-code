import os
import sys
from time import sleep

import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))

a = pg.mixer.Sound('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\audio\\shoot.wav')

pg.mixer.music.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\audio\\moonlight.wav')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.2)

red_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\healthbar.png')
green_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\health.png')
h = 194
running = True
exit_code = False
while running:
    screen.fill((255, 255, 255))

    # font = pg.font.Font(None, 24)
    # text = font.render(str((90000 - pg.time.get_ticks()) // 1000 // 60) + ':' + str((90000 - pg.time.get_ticks()) // 1000 % 60), True, (0, 0, 0))
    # text_rect = text.get_rect()
    # screen.blit(text, text_rect)

    screen.blit(red_img, (5, 5))
    for i in range(h):
        screen.blit(green_img, (i + 8, 8))
    sleep(1)
    h -= 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            a.play()

    if pg.time.get_ticks() >= 9000:
        running = False
        exit_code = True
    elif h <= 0:
        running = False
        exit_code = False

    pg.display.flip()
win_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\youwin.png')
lose_img = pg.image.load('C:\\Users\\puras\\workspace\\proj\\puras\\puras-code\\python\\pygame\\城堡保卫战\\resources\\images\\gameover.png')
if exit_code:
    screen.blit(win_img, (0, 0))
else:
    screen.blit(lose_img, (0, 0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.flip()