import pygame, sys, time, random
from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()
fps = 30

# Initializing global variables/names
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
GREEN = (0, 255, 0)

SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("player_drones Fight On Mars")
pygame.mixer.init()


class Player():
    def __init__(self, img, x, y, width, height, sound):
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.x = x 
        self.y = y
        self.sound = sound

    def play_sound(self):
        # pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.sound))
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()
        # pygame.mixer.Sound(self.sound).play()


class Fire():
    def __init__(self, img, width, height, sound):
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.sound = sound

    def play_sound(self):
        # pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.sound))
        # pygame.mixer.music.load(self.sound)
        # pygame.mixer.music.play()
        pygame.mixer.Sound(self.sound).play()


class Background():
    def __init__(self, img, x, y, width, height):
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.x = x
        self.y = y


class Enemy():
    def __init__(self, img, x, y, width, height, sound):
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.x = x
        self.y = y
        self.sound = sound


def text_screen(text, txtsize, x, y, color):
    font = pygame.font.SysFont(None, txtsize)
    txt_screen = font.render(text, True, color)
    SURFACE.blit(txt_screen, (x, y))

player_drone = Player("drone1.png", 20, 400, 250, 140, "fly.wav")
enemy_drone = Enemy("drone2.png", 1000, 100, 110, 50, "fly.wav")
gun = Fire("gunfire.png", 70, 50, "gunfire.mp3")
missle = Fire("missilebomb.png", 30, 10, "mud-bomb.mp3")
bkgd1 = Background("background1.png", 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
bkgd2 = Background("background2.png", 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
tank = Enemy("tank.png", 1000, 400, 100, 60, "mud-bomb.mp3")

def main_game_loop():
    # main game loop
    direction1 = None
    direction2 = None
    rel_bkg1_x = None
    rel_bkg2_x = None
    player_drone_start = False
    missle_lauch = False
    move_tank = False
    move_enemy_drone = False
    tank_init = time.time()
    tank_rand_time = random.randint(1, 4)
    gun_fire = False
    score = 0

    while True:
        # changing game state according to the events
        SURFACE.fill((0, 0, 0))

        if player_drone_start:
            player_drone.play_sound()

        if bkgd1.x == 0:
            SURFACE.blit(bkgd1.img, (bkgd1.x, bkgd1.y))

        if direction1 == "up" and player_drone.y > 0 :
            player_drone.y -= 5
            
        elif direction1 == "down" and player_drone.y < 400:
            player_drone.y += 5
            if player_drone.y == SCREEN_HEIGHT - 100:
                
                    SURFACE.blit(bkgd1.img, (bkgd1.x, bkgd1.y))
                    SURFACE.blit(bkgd2.img, (rel_bkg1_x, bkgd2.y))
                    print("Yes1! player_drone.y is equal to 400", bkgd1.x, bkgd1.y, bkgd2.x, bkgd2.y, rel_bkg1_x)
                    
                    SURFACE.blit(bkgd2.img, (bkgd2.x, bkgd2.y))
                    SURFACE.blit(bkgd2.img, (rel_bkg2_x, bkgd2.y))

                    if bkgd2.x == - bkgd2.width:
                        SURFACE.blit(bkgd2.img, (rel_bkg2_x, bkgd2.y))
                    print("Yes2! player_drone.y is equal to 400", bkgd1.x, bkgd1.y, bkgd2.x, bkgd2.y, rel_bkg2_x)

        if direction2 == "right" and player_drone.y < SCREEN_HEIGHT - 100:
            if bkgd1.x == 0 and player_drone.x < 100:
                player_drone.x += 5

            elif bkgd1.x != - bkgd1.width:
                SURFACE.blit(bkgd1.img, (bkgd1.x, bkgd1.y))

                rel_bkg1_x = bkgd1.x + bkgd1.width
                SURFACE.blit(bkgd2.img, (rel_bkg1_x, bkgd2.y))

                bkgd1.x -= 5
            
            else:
                SURFACE.blit(bkgd2.img, (bkgd2.x, bkgd2.y))

                rel_bkg2_x = bkgd2.x + bkgd2.width 
                SURFACE.blit(bkgd2.img, (rel_bkg2_x, bkgd2.y))

                if bkgd2.x == - bkgd2.width:
                    SURFACE.blit(bkgd2.img, (rel_bkg2_x, bkgd2.y))
                    bkgd2.x = 0
                bkgd2.x -= 5

        elif direction2 == "left" and player_drone.y < SCREEN_HEIGHT - 100:
            if bkgd1.x == 0 and player_drone.x > bkgd1.x + 100:
                player_drone.x -= 5

            elif bkgd1.x != - bkgd1.width and bkgd1.x < 0:
                bkgd1.x += 5
                SURFACE.blit(bkgd1.img, (bkgd1.x, bkgd1.y))
                rel_bkg1_x = bkgd1.x + bkgd1.width
                SURFACE.blit(bkgd2.img, (rel_bkg1_x, bkgd2.y))
            
            elif bkgd1.x == - bkgd1.width:
                bkgd2.x += 5
                SURFACE.blit(bkgd2.img, (bkgd2.x, bkgd2.y))
                
                rel_bkg2_x = bkgd2.x + bkgd2.width 
                SURFACE.blit(bkgd2.img, (rel_bkg2_x, bkgd2.y))

                if bkgd2.x == 0:
                    SURFACE.blit(bkgd2.img, (rel_bkg2_x, bkgd2.y))
                    bkgd2.x = - bkgd2.width
        
        if missle_lauch:
            missle.y += 5
            
            if missle.y > 400:
                missle_lauch = False
                blast = pygame.transform.scale(pygame.image.load("blast.png"), (200, 160))
                SURFACE.blit(blast, (missle.x, missle.y))
                missle.play_sound()
            
        else:
            missle.x = player_drone.x + 78
            missle.y = player_drone.y + 70

        if move_tank:
            if bkgd1.x == - bkgd1.width:
                if tank.x < - 100 or tank.x - 30 < missle.x and tank.x + 60 > missle.x and tank.y + 50 > missle.y and tank.y < missle.y:
                    tank.x = 1000
                    move_tank = False
                    tank_init = time.time()
                    tank_rand_time = random.randint(1, 4)
                    score += 10

                elif direction2 == "right":
                    tank.x -= 7
                elif direction2 == "left":
                    tank.x -= 2
               
        elif time.time() - tank_init > tank_rand_time:
            move_tank = True

        if bkgd1.x == - bkgd1.width:
            if direction2 == "right":
                enemy_drone.x -= 7
            elif direction2 == "left":
                enemy_drone.x -= 2
            if gun_fire:
                blast = pygame.transform.scale(pygame.image.load("blast.png"), (200, 160))
                SURFACE.blit(blast, (enemy_drone.x, enemy_drone.y))
                enemy_drone.x = 1000
                score += 5
                gun_fire = False
            
            if enemy_drone.x < -100:
                enemy_drone.x = 1000

        # handling events
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    player_drone_start = True
                    
                    if event.key == K_UP:
                        direction1 = "up"
                        
                    elif event.key == K_DOWN:
                        direction1 = "down"
                        
                    elif event.key == K_RIGHT:
                        direction2 = "right"
                        
                    elif event.key == K_LEFT:
                        direction2 = "left"
                        
                    elif event.key == K_f:
                        gun.x = player_drone.x + 110
                        gun.y = player_drone.y + 32
                        SURFACE.blit(gun.img, (gun.x, gun.y))
                        gun.play_sound()     
                        
                        if enemy_drone.x < SCREEN_WIDTH and enemy_drone.x > player_drone.x and enemy_drone.y - 10 < player_drone.y and enemy_drone.y + 100 > player_drone.y:
                            gun_fire = True

                    elif event.key == K_a:
                        missle_lauch = True
        

        SURFACE.blit(player_drone.img, (player_drone.x, player_drone.y))
        SURFACE.blit(missle.img, (missle.x, missle.y))
        SURFACE.blit(enemy_drone.img, (enemy_drone.x, enemy_drone.y))
        SURFACE.blit(tank.img, (tank.x, tank.y))
        text_screen(f"Score: {score}", 50, 700, 25, GREEN)   
        
        pygame.display.update()
        fpsClock.tick(fps)


main_game_loop()


