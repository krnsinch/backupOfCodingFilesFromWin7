import sound
import os
import pygame
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
fps = 30
SURF_WIDTH = 400
SURF_HEIGHT = 600
SURF = pygame.display.set_mode((SURF_WIDTH, SURF_HEIGHT))
pygame.display.set_caption("")
running = True

def display_font(text, textcolor):
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(text, True, textcolor)
    return text
    
a = 0
x = 0
y = 0
sound.play("comphack.mp3", -1)
while running:
    text = display_font(f"FILE address.. {a*3.4/0.34} HACKED.. {a/235}...", "red")
    SURF.blit(text, (x, y))
    fpsClock.tick(fps)
    pygame.display.update()

    a += 1.78
    y += text.get_height() 

    if y > SURF_HEIGHT:
        raise SystemExit

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            raise SystemExit
            
        