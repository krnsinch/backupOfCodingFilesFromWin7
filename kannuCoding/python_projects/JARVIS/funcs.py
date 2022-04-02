import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr
import os
from datetime import datetime
import time
import random
import win32gui, win32con
import mouse, keyboard

vA_name = "fryday"  # virtual assistants's name
medium = None
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)


def get_all_files(directory):
    all_files = []
    dirs = os.listdir(directory)
    
    for entry in dirs:
        entry = os.path.join(directory, entry)

        if os.path.isdir(entry):
            all_files += get_all_files(entry)

        elif os.path.isfile(entry):
            all_files.append(entry)

    return all_files    


def speak(str):
    """speaks any string given as an argument"""
    engine.say(str)
    engine.runAndWait()


def print_and_speak(string):
    print(string)
    speak(string)


def wish_me():
    hour = datetime.now().hour

    if hour >= 0 and hour < 12:
        print_and_speak("\nGood Morning!")
    elif hour >= 12 and hour < 18:
        print_and_speak("\nGood Afternoon!")
    else:
        print_and_speak("\nGood Evening!")

    print_and_speak(f"Its {datetime.now().strftime('%A %d %b %Y')}\
, timing - {datetime.now().strftime('%I:%M')}")
    print_and_speak(f"I am {vA_name} Sir, your virtual assistant. How can I help you?")


def min_max_win(winmode):
    if winmode == "min":
        minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(minimize, win32con.SW_MINIMIZE)

    elif winmode == "max":
        maximize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(maximize, win32con.SW_MAXIMIZE)

    elif winmode == "restore":
        restore = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(restore, win32con.SW_RESTORE)


def chrome_open(url):
    chrome_path = "C:\Program Files\Google\Chrome\Application\Chrome.exe"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open_new_tab(url)


def takecommand():
    """Takes input through given medium and returns it as str"""

    if medium == "k":
        query = input("\nUser: ")

    elif medium == "m":
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.energy_threshold = 500
            recognizer.pause_threshold = 0.6

            while True:
                print("\nListening...")
                try:
                    audiodata = recognizer.listen(source)
                    print("Recognizing...")
                    query = recognizer.recognize_google(
                        audiodata, language="en-in")
                    print(f"User: {query}")
                    break
                except:
                    pass
    return query


def task_execute():
    
    while True:
        try:
            query = takecommand().lower()

# =================================================================
            # running files/apps
            if "open file explorer" in query or "open library" in query or "open libraries" in query:
                print_and_speak("Opening file explorer...")
                os.system("explorer.exe")

            elif "open vs code" in query:
                print_and_speak("Opening Visual Studio Code...")
                os.startfile("C:\Program Files\Microsoft VS Code\Code.exe")

            elif "open photoshop" in query:
                print_and_speak("Opening Adobe Photoshop 7.0...")
                os.startfile(
                    "C:\Program Files\Adobe\Photoshop 7.0\Photoshop.exe")

            elif "open paint" in query:
                print_and_speak("Opening Paint...")
                os.system("mspaint.exe")

            elif "open chrome" in query:
                print_and_speak("Opening Google Chrome...")
                os.startfile("C:\Program Files\Google\Chrome\Application\Chrome.exe")

# =================================================================
            # opening folders
            elif "open user" in query:
                print_and_speak("Opening User folder...")
                os.startfile("c:\\users\\INDIAN")

            elif "open documents" in query:
                print_and_speak("Opening Documents...")
                os.startfile("c:\\users\\INDIAN\\documents")

            elif "open music" in query:
                print_and_speak("Opening Music...")
                os.startfile("c:\\users\\INDIAN\\music")

            elif "open downloads" in query:
                print_and_speak("Opening Downloads...")
                os.startfile("c:\\users\\INDIAN\\downloads")

            elif "open pictures" in query:
                print_and_speak("Opening Pictures...")
                os.startfile("c:\\users\\INDIAN\\pictures")

            elif "open videos" in query:
                print_and_speak("Opening Vidoes...")
                os.startfile("c:\\users\\INDIAN\\Videos")

            elif "open desktop" in query:
                print_and_speak("Opening Desktop...")
                os.startfile("c:\\users\\INDIAN\\desktop")

            elif "open c" in query:
                print_and_speak("Opening local disk c: ...")
                os.startfile("c:")

            elif "open d" in query:
                print_and_speak("Opening local disk d: ...")
                os.startfile("d:")

            elif "open e" in query:
                print_and_speak("Opening local disk e: ...")
                os.startfile("e:")

            elif "open f" in query:
                print_and_speak("Opening local disk f: ...")
                os.startfile("f:")

# =================================================================
            # opening and searching websites
            elif "open" in query:
                if "google" in query:
                    query = "google.com"

                elif "youtube" in query:
                    query = "youtube.com"

                elif "stackoverflow" in query:
                    query = "stackoverflow.com"
                
                elif "github" in query:
                    query = "github.com"
                    
                else:
                    query = query.replace("open ", "")

                print_and_speak(f"Opening {query}...")
                chrome_open(query)

            elif "search" in query:
                query = query.replace("search", "")
                print_and_speak(f"Searching...")

                if "youtube" in query:
                    if "on youtube" in query:
                        query = query.replace("on youtube", "")
                    else:
                        query = query.replace("youtube" , "")
                        
                    chrome_open("youtube.com")
                    time.sleep(10)
                    min_max_win("max")
                    time.sleep(1)
                    mouse.move(460, 125)
                    mouse.click() 
                    keyboard.write(query, 0.02)
                    keyboard.write("\n")
                    
                else:
                    os.startfile("C:\Program Files\Google\Chrome\Application\Chrome.exe")
                    time.sleep(10)
                    min_max_win("max")
                    time.sleep(1)
                    mouse.move(180, 50)
                    mouse.click() 
                    keyboard.write(query, 0.02)
                    keyboard.write("\n")

            elif "wikipedia" in query:
                print_and_speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                fulresult = wikipedia.summary(query)
                print(f"According to Wikipedia,\n\t{fulresult}")
                speak(f"here is some result. According to Wikipedia,\n\t{result}")

                
# =================================================================
            # playing musics
            elif "play " in query:
                musics_path1 = "C:\\users\\indian\\music"
                musics_path2 = "C:\\users\\public\\music"
                musics = get_all_files(musics_path1) + get_all_files(musics_path2)

                if "play music" in query:
                    print_and_speak("Which music do you want to listen?")
                    music = takecommand().lower()

                    if "any" in music:
                        random_music = random.choice(musics)
                        music_name = os.path.basename(random_music)
                        print_and_speak(f"Ok Sir! playing {music_name}...")
                        os.startfile(random_music)

                    else:
                        for i in musics:
                            music_name = os.path.basename(i)

                            if music in music_name.lower():
                                print_and_speak(f"Playing {music_name}...")
                                os.startfile(f"{i}")
                                music_present = True
                                break
                            else:
                                music_present = False

                        if music_present == False:
                            print_and_speak("This music is not present!")

                else:
                    music = query.replace("play ", "")
                    # music = query[(query.index("play ") + len("play ")):]
                    
                    if "any" in music:
                        random_music = random.choice(musics)
                        music_name = os.path.basename(random_music)
                        print_and_speak(f"Ok Sir! playing {music_name}...")
                        os.startfile(f"{random_music}")

                    else:
                        for i in musics:
                            music_name = os.path.basename(i)
                            
                            if music in music_name.lower():                                
                                print_and_speak(f"Playing {music_name}...")
                                os.startfile(f"{i}")
                                music_present = True
                                break
                            else:
                                music_present = False

                        if music_present == False:
                            print_and_speak("This music is not present!")

# =================================================================
            # minimize, maximize, restore current foreground window
            elif "minimize this window" in query or "minimise" in query or "min" in query:
                min_max_win("min")

            elif "maximize this window" in query or "maximize" in query or "max" in query:
                min_max_win("max")

            elif "restore this window" in query or "restore" in query or "restore this" in query:
                min_max_win("restore")


# =================================================================
            # date and time
            elif "date" in query:
                print_and_speak(datetime.now().strftime("%A %d %b %Y"))

            elif "time" in query:
                print(str(datetime.now().strftime("%Ih: %Mmin: %Ss")))
                speak(str(datetime.now().strftime("%I:%M:%S")))
                
# =================================================================
            # re-run
            elif "re-run" in query or "re-start" in query:
                print_and_speak("Ok! I am Re-starting...")
                os.startfile("main.py")
                raise SystemExit

# =================================================================  
            # sleep mode
            elif "sleep" in query:
                print_and_speak("Ok Sir! I am going to sleep. You can call me back any time.")
                break

# =================================================================            
            # things jarvis can do
            elif "what can you do" in query:
                print_and_speak("I can do almost all those daily tasks which a programmer generally needs \
to do in his Computer, like, opening Google, Youtube, Chrome, Edge, or any website, searching something from Wikipedia, opening any app from your pc\
, playing musics and telling date and time, etc.")

# =================================================================
            # for quitting
            elif "quit" in query or query == "q":
                print_and_speak("Ok Sir! Quiting...")
                raise SystemExit

            else:
                print_and_speak(
                    "Sorry sir, I cannot do this task as I am not programmed for this task!")

        except Exception as e:
            print_and_speak(f"Some error occured (error: {e})")


