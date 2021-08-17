import datetime
import random
import time
import os
import subprocess
import platform
from funx import readfile, wget, writefile

config = readfile('config/settings.json')
last_session = readfile("config/.last_session")

name = config["Name"]
user = config["Nickname"]
ai = config["AI Name"]
username = config["username"]
password = config["password"]

last_time = datetime.datetime.now().strftime("%d-%m-%Y %a, %I:%M:%S %p")
operating_system = platform.system()
hostname = platform.node()

last_session_file = open("config/.last_session", 'w')
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
        commands = readfile("config/commands.json")
        cmd = input(f"{user}: ").lower()
        try:
            if cmd in commands:
                content = commands[cmd]
                task = content['task']
                task_type = content['type']

                if task_type == 'url':
                    wget(task)

                elif task_type == 'executable':
                    if operating_system == "Windows":
                        subprocess.Popen(task)
                    else:
                        os.system(task)

                elif task_type == "command":
                    os.system(task)

                elif task_type == "file reading":
                    if task == "":
                        print(readfile(input("File: ")))
                    else:
                        print(readfile(task))

                elif task_type == "file writing":
                    file = input("File: ")
                    content = input("Content: ")
                    writefile(content, file)

            elif cmd == "shutdown" or cmd == "poweroff":
                os.system("shutdown -s")

            elif cmd == "restart" or cmd == "reboot":
                os.system('shutdown -r')

            elif cmd == "clear":
                try:
                    os.system("clear")
                except:
                    os.system('cls')

            elif cmd == "exit" or cmd == "quit":
                print("Exiting...")
                time.sleep(2)
                break
            else:
                greeted = False
                basics = readfile('config/basics.json')
                for basic in basics:
                    patterns = basics[basic]["patterns"]
                    response = basics[basic]["response"]
                    for pattern in patterns:
                        if pattern in cmd.split():
                            print(random.choice(response))
                            greeted = True
                            break
                else:
                    if not greeted:
                        print(f"{ai}: Command not found: {cmd}")

        except Exception as error:
            print(f"{ai}: {error}")


if __name__ == "__main__":
    app()
