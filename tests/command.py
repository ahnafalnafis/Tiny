import json

with open("url-opening.json") as commandsFile:
    commands = json.load(commandsFile)

from funx import wget

cmd = input(">> ").lower()

link = commands[cmd]
wget(link)
