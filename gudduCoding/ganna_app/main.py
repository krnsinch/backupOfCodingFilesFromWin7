from os import name
import tkinter as tk
from tkinter import*
from tkinter.font import BOLD, Font
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

root = tk.Tk()

# Setting a window
root.geometry("600x350")

# Setting a title
root.title("Music Platform")

# lable 
lble = Label(root , text="Ganna-App",font=("Andalus","25"))
lble.pack()
lble.place(x=220,y=30)

# search box
search= Label(root ,text="search")
search.grid(row=16,column=29)
searchvalue = StringVar
search_entry = Entry(root ,textvariable = searchvalue )
# search_entry.grid(row=28,column=16)


root.mainloop()

