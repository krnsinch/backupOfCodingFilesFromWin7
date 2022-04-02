import os
import time
import sound
import pygame

def main(stop=0):
    sound.play("comphack.mp3", -1)
    a = 0
    while a < 100:
        print(f"initializing all folder{a/0.332} and files{a/0.342}...")
        time.sleep(0.05)
        a += 1
    print("\t\t\tALL FOLDER AND FILES ARE INITIALISED!")

    time.sleep(1)
    os.startfile("v2.py")

    pygame.mixer.init()
    sound2 = pygame.mixer.Sound("compHacking.mp3")
    sound2.play()

    time_init = time.time()
    while True:
        if (time.time() - time_init) > 30:
            sound2.stop()
            return

main()


