import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('hello world')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()