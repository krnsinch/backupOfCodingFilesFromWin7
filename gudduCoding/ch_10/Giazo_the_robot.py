import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(str):
    engine.say(str)
    engine.runAndWait()


class Robot:
    name = "robot"
    height = 5.43 
    body =  "Nitrain"
    name = "Chigago"

    def image_mesg(self):
        """returns first message with image"""
        return f"""
           o  o
           \\_/
           |o o|_
           |_____|  Hello I am a animal robot.
           | |       My name is {self.name}.
   +    ___| |         How are you?
   \\__|______/         
      / \\  / \\
"""

    def talk(self):
        speak(f"Hello I am a animal robot. My name is {self.name}. How are you?")
        speak("How,are,you,guddu")
guddu = Robot() 
guddu.name = "Giazo"
print(guddu.image_mesg())
guddu.talk()


class Command:    
        """ask  a command and return I am walking"""
        user = str(input("Give me command," ))
        def ask_command(self , sleep , run , walk , read):
            self.sleep = sleep
            self.walk = walk
            self.read = read
            self.run = run

        if 'walk' in user:
            print('I am Walking')
            speak("Ok,guddu,I am Walking")
        elif 'sleep' in user:
           print('I am going to sleep')
        elif 'run' in user:
            print('Ok! I am running')
        elif 'read' in user:
            print('I am read something')
            
       

c = Command()
c.ask_command('I am going to sleep','Ok! I am running','I am Walking','I am read something')





