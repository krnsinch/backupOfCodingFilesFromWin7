import sound
import os
import pygame
from pygame.locals import *
import time

pygame.init()

fpsClock = pygame.time.Clock()
fps = 30
SURF_WIDTH = 400
SURF_HEIGHT = 600
SURF = pygame.display.set_mode((SURF_WIDTH, SURF_HEIGHT))
pygame.display.set_caption("")
running = True
sound.play("comphack.mp3", -1)
def display_font(text, textcolor):
    font = pygame.font.Font("freesansbold.ttf", 15)
    text = font.render(text, True, textcolor)
    return text

a = 0
b = 0 
x = 0
y = 0

texts = [display_font("Getting Accessing...", "green"), display_font("Got access...", "green"), 
display_font("Getting into Operating_System...", "green"), display_font("Collecting all DATA...", "green"), 
display_font("HACKED!...", "green")]

for text in texts:
        SURF.blit(text, (x, y))
        fpsClock.tick(fps)
        pygame.display.update()
        y += text.get_height()
        time.sleep(2)

while running:
    text = display_font(f"c:d_<?%&{y/23479}xy03_~!as{45*0.3/y}", "orange")
    SURF.blit(text, (x, y))
    fpsClock.tick(fps)
    pygame.display.update()
    y += text.get_height()

    if y > SURF_HEIGHT:
        os.startfile("v5.py")
        raise SystemExit
    
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
   
        
        