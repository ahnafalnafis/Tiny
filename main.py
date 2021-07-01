import datetime
import time
import os
from functions import readfile, speak, wget

ai = readfile('Settings/settings.json')
ai = ai["AI Name"]


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
            for cmd in cmds:
                task = cmds[cmd]
                if cmd in command:
                    try:
                        os.system(f"{task}")
                    except:
                        wget(task)

            if 'clear' in command:
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
