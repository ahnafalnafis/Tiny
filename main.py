import datetime
import time
import os
import platform
from functions import readfile, wget

settings = readfile('Settings/settings.json')
last_session = readfile("Settings/.last_session")

name = settings["Name"]
user = settings["Nickname"]
ai = settings["AI Name"]
username = settings["username"]
password = settings["password"]

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
operating_system = platform.system()

print(f"You have now logged in from {operating_system} at {hour}:{minute}:{second}")
last_session_file = open("Settings/.last_session", 'w')
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

#### Voice mode is disabled temporarily. It will be enabled in future.
# def greetUserV():
#     hour = int(datetime.datetime.now().hour)

#     if hour >= 0 and hour < 12:
#         speak(f"Good Monring!")

#     elif hour >= 12 and hour < 18:
#         speak(f"Good After Noon!")

#     else:
#         speak(f"Good Evening!")


def app():
    while True:
        commands = readfile("Settings/commands.json")
        cmd = input(f"{user}: ").lower()
        try:
            try:
                content = commands[cmd]
                print(content)
                task = content["task"]
                print(task)
                alt = content["alt"]
                type = content["type"]
                if type == 'url':
                    print('es')
                    wget(task)
                elif type == "executable":
                    try:
                        os.system(task)
                    except:
                        os.system(alt)
            except:
                if 'clear' in cmd:
                    try:                
                        os.system("clear")
                    except:
                        os.system('cls')

                elif 'exit' in cmd or 'quit' in cmd or 'bye' in cmd:
                    print("Have a nice day 😊. \nGood bye.\nExiting ")
                    time.sleep(5)
                    break

                else:
                    print(f"{ai}: Command not found: {cmd}")
        except Exception as error:
            print(f"{ai}: {error}")
            print(f"{ai}: Command not found: {cmd}")


app()
