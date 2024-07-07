import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('hello world')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            # sys.exit()
            running = False

pygame.quit()
sys.exit()