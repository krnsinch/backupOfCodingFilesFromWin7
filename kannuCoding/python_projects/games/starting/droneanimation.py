import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("believer.mp3")
pygame.mixer.music.play(-1)

fps = 30 # setting frames per second
fpsClock = pygame.time.Clock()

# setting up the window
SURFACE = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Drone Animation")

droneSurfObj = pygame.image.load("drone.png")
dronex = 10
droney = 10
direction = "right"

# main game loop
while True:
    SURFACE.fill((186, 200, 153))
    
    if direction == "right":
        dronex += 2
        if dronex == 600:
            direction = "down"
    
    elif direction == "down":
        droney += 2
        if droney == 400:
            direction = "left"
        
    elif direction == "left":
        dronex -= 2
        if dronex == 10:
            direction = "up"
    
    elif direction == "up":
        droney -= 2
        if droney == 10:
            direction = "right"

    SURFACE.blit(droneSurfObj, (dronex, droney))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                fps += 20
            elif event.key == K_s and fps > 20:
                fps -= 20

            if event.key == K_j:
                droneSurfObj = pygame.transform.scale(pygame.image.load("drone2.png"), (100, 50))
            elif event.key == K_l:
                droneSurfObj = pygame.image.load("drone.png")
            
                
    pygame.display.update()
    fpsClock.tick(fps)




