import pygame, sys
from pygame.locals import *

pygame.init()

# setup the window
SURFACE = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Drawing Shapes")

# setup colors
BLACK = (0, 0, 0)
LIGHTBROWN = (96, 168, 240)
BLUE = (0, 0, 255)
PINK = (200, 105, 90)
GREEN = (151, 243, 67)
ORANGE = (234, 137, 49)

# draw on the surface object
SURFACE.fill((207, 197, 175))
pygame.draw.polygon(SURFACE, LIGHTBROWN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(SURFACE, BLUE, (20, 40), (500, 160), width=5)
pygame.draw.lines(SURFACE, BLUE, True, [(230, 5), (42, 100), (150, 7)])
pygame.draw.circle(SURFACE, PINK, (400, 300), 50)
pygame.draw.ellipse(SURFACE, ORANGE, (234, 150, 500, 300))
pygame.draw.rect(SURFACE, GREEN, (500, 250, 200, 100))

pixObj = pygame.PixelArray(SURFACE)

pixObj[480][380] = BLACK

pixObj[482][382] = BLACK

pixObj[484][384] = BLACK

pixObj[486][386] = BLACK

pixObj[488][388] = BLACK

del pixObj


# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




