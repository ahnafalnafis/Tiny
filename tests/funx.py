import webbrowser
import random
import json
from time import sleep


def wget(url):
    """Opens url in browser"""
    webbrowser.open(url)


def readfile(file):
    """Reads both json and Plain text file and returns the content of the given file"""
    if file.endswith(".json"):
        with open(file) as handler:
            content = json.load(handler)
    else:
        handler = open(file, 'r')
        content = handler.read()
        handler.close()
    return content


def writefile(content, file):
    """Writes the content to the given file"""
    handler = open(file, 'w')
    handler.write(content)
    handler.close()


def verify(username, password):
    uname = readfile('config/settings.json')
    uname = uname["username"]
    passwd = readfile('config/settings.json')
    passwd = passwd["password"]

    if username != uname or password != passwd:
        print("Verification failed. Incorrect username or password.")
        sleep(10)
        exit()


def sudo():
    attempt_count = 0
    attempt_limit = 3
    uname = readfile('config/settings.json')
    uname = uname["username"]
    passwd = readfile('config/settings.json')
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


#######################################################
# Spell Checker:
#######################################################
def read_dict_file(file_name):
    words = list()
    fhand = open(file_name)
    for line in fhand:
        word = line.strip()
        words.append(word)
    fhand.close()
    return words


def read_text(text):
    words = list()
    all_words = text.split()
    for word in all_words:
        words.append(word.strip(".,!\"':;?").lower())
    return words


def find_misspelled(dict_words, words):
    misspelled = list()
    for word in words:
        if word not in dict_words:
            misspelled.append(word)
    return misspelled


def spell_check(text):
    print("Checking...")
    dict_file = "dictionary.txt"
    dict_words = read_dict_file(dict_file)
    error_list = find_misspelled(
        dict_words, read_text(text))

    print("Misspelled words: ")
    for word in error_list:
        print(word)


#######################################################
