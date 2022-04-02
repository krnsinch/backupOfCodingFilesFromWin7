import pygame
pygame.mixer.init()

def play(music, loop=0):
    sound = pygame.mixer.Sound(music)
    sound.play(loop)
