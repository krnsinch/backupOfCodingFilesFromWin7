import pygame, sys, random
from pygame.locals import *
import time

# initializing all modules in pygame
pygame.init()

# setting fps and Clock obj
FPS = 60
FPSCLOCK = pygame.time.Clock()

# setting up window
surf_x = 800
surf_y = 600 
SURFACE = pygame.display.set_mode((surf_x, surf_y))
pygame.display.set_caption("Snake game")

# setting colors
GREEN = (30, 105, 50)
RED = (255, 0, 0)
PURPLE = (163, 73, 164)

def text_screen(text, color, x, y, txt_size):
    font = pygame.font.SysFont(None, txt_size)
    screen_txt = font.render(text, True, color)
    SURFACE.blit(screen_txt, (x, y))

def plot_snk(surface, color, snklist, snksize):
    for x, y in snklist:
        pygame.draw.rect(surface, color, (x, y, snksize, snksize))
    
# main game loop
def main_game_loop():
    FPS = 60
    FPSCLOCK = pygame.time.Clock()

    # setting up window
    surf_x = 800
    surf_y = 600 
    SURFACE = pygame.display.set_mode((surf_x, surf_y))
    pygame.display.set_caption("Snake game")

    # setting colors
    GREEN = (30, 105, 50)
    RED = (255, 0, 0)
    PURPLE = (163, 73, 164)

    snake_x = 10
    snake_y = 250
    snakeSize = 20

    food_x = random.randint(50, 750)
    food_y = random.randint(50, 550)
    foodSize = 15

    bigFood_size = 25
    bigFood_init = time.time()
    bigFood_x = random.randint(50, 750)
    bigFood_y = random.randint(50, 750)

    direction = "right"
    score = 0
    snklist = []
    snklen = 1
    snksize = 20
    removeBigFood_init = time.time()

    game_over = False

    while True:
        SURFACE.fill((0, 0, 0))
        if game_over:
            text_screen("Game Over!", RED, 300, 200, 50)
            text_screen(f"Your score - {score}", RED, 290, 240, 50)
            text_screen("Press enter to play again", RED, 200, 270, 50)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == K_RETURN:
                        main_game_loop()

        else:
            if direction == "right":
                snake_x += 5
            elif direction == "left":
                snake_x -= 5
            elif direction == "up":
                snake_y -= 5
            elif direction == "down":
                snake_y += 5
            
            if snake_x == 0 or snake_y == 0 or snake_x == surf_x or snake_y == surf_y:
                game_over = True
                    
            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 2
                food_x = random.randint(50, 750)
                food_y = random.randint(50, 550)
                snklen += 5
                
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if direction == "up" or direction == "down":
                        if event.key == K_a:
                            direction = "left"
                        elif event.key == K_d:
                            direction = "right"

                    elif direction == "right" or direction == "left":
                        if event.key == K_w:
                            direction = "up"
                        elif event.key == K_s:
                            direction = "down"
                    
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snklist.append(head)

            if len(snklist) > snklen:
                del snklist[0]

            plot_snk(SURFACE, GREEN, snklist, snksize)

            text_screen(f"Score: {score}", GREEN, 10, 10, 55)
            
            pygame.draw.rect(SURFACE, PURPLE, (food_x, food_y, foodSize, foodSize))

            if time.time() - bigFood_init > 15:
                pygame.draw.rect(SURFACE, RED, (bigFood_x, bigFood_y, bigFood_size, bigFood_size))

                if time.time() - removeBigFood_init < 22:
                    if abs(snake_x - bigFood_x) < 25 and abs(snake_y - bigFood_y) < 25:
                        score += 10
                        bigFood_x = random.randint(50, 750)
                        bigFood_y = random.randint(50, 550)
                        bigFood_init = time.time()
                        removeBigFood_init = time.time()
                    
                elif time.time() - removeBigFood_init > 22:
                    bigFood_x = random.randint(50, 750)
                    bigFood_y = random.randint(50, 550)
                    bigFood_init = time.time()
                    removeBigFood_init = time.time()
                
        # updating the game state according to events
        pygame.display.update()
        FPSCLOCK.tick(FPS)


score = main_game_loop()

    




