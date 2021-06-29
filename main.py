import datetime
import json
from functions import speak

with open('Settings/settings.json') as settings_handler:
    ai = json.load(settings_handler)

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

