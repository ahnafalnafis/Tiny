import json
from os import *

# with open('settings.json') as fh:
#     ai_name = json.load(fh)

# ai_name = ai_name["AI Name"]


# def ai_name_error():
#     if ai_name == "JARVIS" or ai_name == "jarvis" or ai_name == "Jarvis":
#         print("Invalid AI Name. The right of this name is reserved by the creator Sir Ahnaf Al Nafis. Please change the AI Name from settings.json otherwise this program will not execute.")
#         exit()


# ai_name_error()
command = input(">> ").lower()

def readfile(filename):
    with open(filename) as file_handler:
        content = json.load(file_handler)
        return content


# urlcmds = readfile("url-opening.json")
# print(urlcmds)

# for k in urlcmds:
#     print(k)
#     v = urlcmds[k]
#     print(v)

if 'open' in command:
    command = command.replace("open", "").strip()
    print(command)
    if path.isdir(command):
        print(f"yes")

    else:
        print('dd')