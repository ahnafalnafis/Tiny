import webbrowser
import playsound
from gtts import gTTS
import json
from time import sleep


def wget(url):
    webbrowser.open(url)


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def readfile(filename):
    with open(filename) as file_handler:
        content = json.load(file_handler)
        return content


def verify(username, password):
    uname = readfile('Settings/settings.json')
    uname = uname["username"]
    passwd = readfile('Settings/settings.json')
    passwd = passwd["password"]

    if username != uname or password != passwd:
        print("Verification failed. Incorrect username or password.")
        sleep(10)
        exit()


def sudo():
    attempt_count = 0
    attempt_limit = 3
    uname = readfile('Settings/settings.json')
    uname = uname["username"]
    passwd = readfile('Settings/settings.json')
    passwd = passwd["password"]
    while attempt_count < attempt_limit:
        password = input(f"[sudo] password for {uname}: ")
        attempt_count += 1
        if password == passwd:
            break
        else:
            print("Sorry, try again")
    else:
        print("sudo: 3 incorrect password attempts")
