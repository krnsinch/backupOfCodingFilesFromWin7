import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Set voice.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#  speak Function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wishing Function
def wishMe():
    hour = int(datetime.datetime.now() .hour)
    if hour>= 0 and hour<12:
        speak("Hello,Good Morning! ")
    elif hour>=12 and hour<18:
            speak("Hello,Good Afternoon!")
    else:
        speak("Hello , Good Evening! ")

    speak(" I am AI virtual robot assistant named, Zira")
    print("How can I help you")

# Take Command Function
def takeCommand():
    '''  It takes input from the user and returns string objects. '''
    query = input("User: ")
    return query

if __name__ == "__main__":
    wishMe()


    while True:
        query = takeCommand().lower()
# Logic for executing input based on query.
      #  Task 1: for shut down the assistant.
        if'sleep'in query:
            speak("shut down")
            break

    # Task 2: search something in wikipedia 
        elif 'wikipedia' in query:
            speak('Searching Wikipedia..............')
            query = query.replace('wikipedia',' ')
            results = wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia...') 
            print(results) 
            speak(results)  

        elif 'hello'in query:
           speak("Hello , Nice to meet you . How can I help you ") 
           print("Hello ,Nice to meet you😃\n>>>How can I help you") 


    # Task 3 : open youTube in web browser.
        elif 'open youtube' in query:
            print("Opening youtube..."); speak("Opening youtube...")
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\Chrome.exe"))
            webbrowser.get("chrome").open("youtube.com")


    # Task 4: open google site in web browser.
        elif 'open google' in query:
            print("Opening google..."); speak("Opening google...")
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\Chrome.exe"))
            webbrowser.get("chrome").open("google.com")


    # Task 5: open stack overflow site in web browser.
        elif 'open stackoverflow' in query:
            print("Opening stackoverflow..."); speak("Opening stack overflow...")
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\Chrome.exe"))
            webbrowser.get("chrome").open("stackoverflow.com")


    # Task 6 : Play Music.
        elif 'play music' in query:
            music_dir =  "c:\\users\\user\\music\\fav_musics"
            songs = os.listdir(music_dir)     # the listdir() is list all the presnt file in music_dir.
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

    
    #  Task 7: To know current Time.
        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}") 
            print(f"The time is {strTime}") 

            
    # Task 8: To open VS code.
        elif 'open vs code' in query :
            speak("Opening Visul Studio code........... ")
            speak("Process is running...\nPlease wait.")
            pro_path = os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
            print(pro_path)

    
    # Task 9: To open paint.
        elif 'open paint' in query:
            speak("OK . Opening paint")
            print("Opening paint........")
            paint_path = os.system("mspaint.exe")
            print(paint_path)


    # Task 10: If say thank you.
        elif 'thank you' in query:
            speak("Its my pleasure! ")
            print("welcome******************")


    # Task 11: To open calculator.
        elif 'open calculator' in query:
            speak("opening calculator..........")
            cal_path = os.startfile("C:\\Users\\User\\Desktop")
            print(cal_path)


    # Task 12 : To open Jarvis.
        elif 'open jarvis' in query:
            speak("open AI . assistant  Jarvis........")
            jar_path = os.startfile("C:\\Users\\User\\Documents\\learnToProgram\\Python_Files\\python_projects\\JARVIS\\main.py")
            print(jar_path)

    #  Task 13: To open Healthy programme.
        elif 'open healthy programmer'in query:
            speak("opening healthy programmer.......")
            hea_path = os.startfile("C:\\Users\\User\\Documents\\learnToProgram\\Python_Files\\python_projects\\Healthy_Programmer\\Healthy Programmer.py")
            print(hea_path)


     #  Task 14 : command is out of programmed.
        else:
            speak("""sorry , i am not be able to do your task . 
            Let i remind you  """)
            print("""1.search something on wikipedia \n2.open youtube\n3.google\n4.open stackoverflow\n5.playing music\n6.Time\n7.open visual studio code\n 8.open paint 
9.open calculator\n10.Jarvis""")
