from funcs import *
import funcs

head = f"""
            {vA_name.upper()} (a virtual assistant)            
How do you want to access {vA_name}?
Enter 'k' for keyboard
Enter 'm' for microphone
Enter 'q' to quit
"""

while True:
    funcs.medium = input(head)
    if funcs.medium == "q":
        raise SystemExit
    elif funcs.medium == "k" or funcs.medium == "m":
        break
    else:
        head = "Invalid input! Please enter from k, m and q\n"

wish_me()
print("(ask me 'what can you do')")
task_execute()

while True:
    # mode (sleep/wake up)
    try:
        query = takecommand().lower()

        if "wake up" in query:
            print_and_speak("Ok Sir! what can i do for you?")
            task_execute()

    except Exception as e:
        print_and_speak(f"Some error occured (error: {e})")
        
