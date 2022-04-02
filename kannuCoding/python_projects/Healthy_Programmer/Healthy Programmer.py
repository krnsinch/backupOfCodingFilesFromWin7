from time import time
from pygame import mixer
mixer.init()

def music_on_loop(message, stopper):
    mixer.music.load("musics\\remind.mp3")
    mixer.music.play(-1)
    print(message)
    str1 = f"Enter {stopper} to stop the reminder\n"

    while True:
        stp = input(str1)

        if stp == "q":
            raise SystemExit
        elif stp == stopper:
            mixer.music.stop()
            break
        else:
            str1 = f"Invalid! enter {stopper} to stop the reminder\n"
            


timers = input("""
___________HEALTHY PROGRAMMER___________

Which reminder(s) to set?
Enter - 'w' for water, 
        'e' for eyes, 
        'p' for physical activity,
        'q' to quit

Reminder(s): """)

while True:
    timersCheck = True
    for i in timers:
        if i != "w" and i != "e" and i != "p" and timers != "q":
            timersCheck = False
            break

    if timersCheck:

        waterInit = time()
        eyesInit = time()
        exInit = time()
        
        waterTime = 60 * 40
        eyesTime = 60 * 15
        exTime = 60 * 60

        while True:
            for i in timers:
                if i == "q":
                    raise SystemExit

                elif i == "w":
                    if time() - waterInit > waterTime:
                        music_on_loop("\nWater drinking time", "w")
                        waterInit = time()
                        
                elif i == "e":
                    if time() - eyesInit > eyesTime:
                        music_on_loop("\nEyes relaxing time", "e")
                        eyesInit = time()

                elif i == "p":
                    if time() - exInit > exTime:
                        music_on_loop("\nPhysical activity time", "p")
                        exInit = time()

    else:
        timers = input(f"Invalid input!\n")
