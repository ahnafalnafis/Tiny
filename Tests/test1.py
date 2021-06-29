import json

with open('settings.json') as fh:
    ai_name = json.load(fh)

ai_name = ai_name["AI Name"]


def ai_name_error():
    if ai_name == "JARVIS" or ai_name == "jarvis" or ai_name == "Jarvis":
        print("Invalid AI Name. The right of this name is reserved by the creator Sir Ahnaf Al Nafis. Please change the AI Name from settings.json otherwise this program will not execute.")
        exit()


ai_name_error()