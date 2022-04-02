import pygame
from pygame.locals import *
import sys

pygame.init()
SURFACE = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Black Pygame")

# main game loop 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
            

