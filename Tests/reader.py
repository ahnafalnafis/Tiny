import json

# with open('settings.json') as settingsFile:
#     settings = json.load(settingsFile)

# Name = settings["Name"]
# FirstName = settings["First Name"]
# LastName = settings["Last Name"]
# Nicname = settings["Nickname"]
# Age = settings["Age"]

# print(f"His full name is {Name}, first name is {FirstName}, last name is {LastName}, nick name is {Nicname} and his age is {Age}")

def readfile(filename):
    with open(filename) as file_handler:
        content = json.load(file_handler)
        return content

print(readfile('settings.json'))