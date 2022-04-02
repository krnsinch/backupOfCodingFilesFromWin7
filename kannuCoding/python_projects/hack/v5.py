import sound
import os, time
import pygame
from pygame.locals import *

pygame.init()


fpsClock = pygame.time.Clock()
fps = 30
SURF = pygame.display.set_mode()
attention = pygame.transform.scale(pygame.image.load("attention.png"), (SURF.get_width(), SURF.get_height()))
sysHackSucess = pygame.transform.scale(pygame.image.load("sysHackSuccessful.png"), (SURF.get_width(), SURF.get_height()))
running = True

def display_font(text, textcolor, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, textcolor)
    return text
    
a = 0
x = 0
y = 0

sound.play("winOpen.mp3")
sound.play("comp_hack2.mp3")

SURF.blit(attention, (x, y))
pygame.display.update()
time.sleep(5)

SURF.fill((0, 0, 0))
#sound.play("comp_hack2.mp3")
SURF.blit(sysHackSucess, (x, y))
fpsClock.tick(fps)
pygame.display.update()

x = 500
y = 330

text = "Your System has been hacked_"
for i in range(len(text)):
    textsurf = display_font(text[i], "green", 27)
    SURF.blit(textsurf, (x, y))
    fpsClock.tick(fps)
    pygame.display.update()
    x += textsurf.get_width()
    time.sleep(0.2)


while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            raise SystemExit
    
    

    
        
        
