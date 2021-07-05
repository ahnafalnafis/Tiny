import datetime
import time
import os
import platform
from functions import readfile, speak, wget

settings = readfile('Settings/settings.json')
last_session = readfile("Settings/.last_session")
ai = settings["AI Name"]
name = settings["Name"]

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
operating_system = platform.system()
print(f"You have now logged in from {operating_system} at {hour}:{minute}:{second}")
last_session_file = open("Settings/.last_session")
last_session_file.write(f"{operating_system} at {hour}:{minute}:{second}")
last_session_file.close()
print(f"You last logged in from {last_session}")

def greetUser():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print(f"{ai}: Good Monring!")

    elif hour >= 12 and hour < 18:
        print(f"{ai}: Good After Noon!")

    else:
        print(f"{ai}: Good Evening!")


def greetUserV():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(f"Good Monring!")

    elif hour >= 12 and hour < 18:
        speak(f"Good After Noon!")

    else:
        speak(f"Good Evening!")


def app():
    user = readfile("Settings/settings.json")
    user = user["Nickname"]
    while True:
        cmds = readfile("Settings/commands.json")
        command = input(f"{user}: ").lower()
        try:
            if 'clear' in command:
                # if operating_system == "linux":
                os.system("clear")

            elif 'exit' in command or 'quit' in command or 'bye' in command:
                print("Exiting")
                time.sleep(2)
                exit()

            else:
                print(f"{ai}: Command not found: {command}")
        except Exception as error:
            print(f"{ai}: Command not found: {error}")


app()
