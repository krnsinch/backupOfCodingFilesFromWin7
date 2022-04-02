from tkinter import *
import pyttsx3, pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("JarvisWelcomeBack.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.load("startup_intro.mp3")
    pygame.mixer.music.play()
    
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty(voices[0], "voice")

def speak(string):
    engine.say(string)
    engine.runAndWait()

root = Tk()  # returns an instance of Tk and display the root window 
             # which manages all the other components of the tkinter application.

root.geometry("600x400")  # sets initial width and height

# root.overrideredirect(1)  # removes head bar
# root.attributes("-alpha", 0.7)  # transparency

root.minsize(200, 100)  # sets minimum size of the window
root.maxsize(800, 600)  # sets maximum size of the window 

text = Label(text="Hello, welcome to New Window!")
#text.pack()

photoimage = PhotoImage(file="image.png")
# photo = Label(image=photoimage, COMMAND=play)
# photo.pack()

play_button = Button(root, image=photoimage, command=play)
play_button.pack(pady=0)

root.mainloop()
#speak("Now let me introduce myself. I am Jarvis, a virtual artificial intelligence.\
#I am with you, 24 into 7, every day a week, everytime, everywhere.")
