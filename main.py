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

last_time = datetime.datetime.now().strftime("%d-%m-%Y %a, %I:%M:%S %p")
operating_system = platform.system()
hostname = platform.node()

last_session_file = open("Settings/.last_session", 'w')
last_session_file.write(f"{operating_system} at {last_time} ")
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


def app():
    while True:
        commands = readfile("Settings/commands.json")
        cmd = input(f"{user}: ").lower()
        try:
            if cmd in commands:
                content = commands[cmd]
                task = content['task']
                type = content['type']
                alt_task = content["alt task"]
                if type == 'url':
                    wget(task)
                elif type == 'executable':
                    if operating_system == 'Windows':
                        os.system(alt_task)
                    else:
                        os.system(task)
            elif 'clear' in cmd:
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
            # print(f"{ai}: Command not found: {cmd}")


app()
