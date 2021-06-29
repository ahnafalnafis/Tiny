import datetime
import webbrowser
import wikipedia
command = ""
ai = "JARVIS"
# Gender = ''
user = "Sir"
i = 0
j = 0
i1 = 0
prt = "https://"
aft = f"Okay,{user}."
nxtcmd = f"Next command {user}."


def greet_me():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print(f"{ai}: Good Monring!")

    elif hour >= 12 and hour < 18:
        print(f"{ai}: Good After Noon!")

    else:
        print(f"{ai}: Good Evening!")


def creator():
    print("""\nName: Ahnaf Al Nafis.
Junior Python Developer and founder of \"Ahnaf Industries\"""")


def me():
    command = input(
        f"I'm {ai}, created by Sir Ahnaf Al Nafis.\n\nAre you want to know more about my creator?(Yes/No): ").lower()
    if command == "yes":
        creator()
    elif command == "no":
        main()


def main():
    while True:
        command = input("You: ").lower()
        # Google:
        if "yt" in command or "youtube" in command:  # YouTube
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}youtube.com")

        elif "gmail" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}gmail.com")

        elif "gtrans" in command or "gt" in command or "google translate" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}translate.google.com")

        elif "gs" in command or "google sties" in command or 'gsites' in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}sites.google.com")

        elif "gdrive" in command or "google drive" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}drive.google.com")

        # Social:
        elif "fb" in command or "facebook" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}facebook.com")

        elif "msngr" in command or "messenger" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}messenger.com")

        elif "wapp" in command or "whatsapp" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}web.whatsapp.com")

        elif "insta" in command or "instagram" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}instagram.com")

        elif "twitter" in command:
            print(f"{ai}: {aft}")
            webbrowser.open(f"{prt}twitter.com")

        # # Apps:
        # elif "vscode" in command or "vs code" in command or "visual studio code" in command:
        #     print(f"{ai}: {aft}")
        #     path = "C:\\Users\\Ahnaf\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(path)
        #     print(nxtcmd)
        # elif "cmd" in command or "command prompt" in command:
        #     print(f"{ai}: {aft}")
        #     path = "C:\\Windows\\System32\\cmd.exe"
        #     os.startfile(path)
        #     print(nxtcmd)
        # elif "word" in command or "ms word" in command or "microsoft word" in command:
        #     print(f"{ai}: {aft}")
        #     path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk"
        #     os.startfile(path)
        #     print(nxtcmd)
        # elif "excel" in command:
        #     print(f"{ai}: {aft}")
        #     path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk"
        #     os.startfile(path)
        #     print(nxtcmd)
        # elif "one note" in command or "1note" in command or "1 note" in command:
        #     print(f'{ai}: {aft}')
        #     print(nxtcmd)
        # # Basic Knowledges
        elif "who are you" in command or "who're you" in command or "who r u" in command:
            me()
        elif "hi" in command or 'hello' in command:
            print(f"{ai}: Yes {user}.")

        elif "how are you" in command or "how're you" in command or "how r u" in command or "how r you" in command or "how are u" in command:
            hru = input(f"{ai}: I'm fine. You?\n")
            if hru == 'fine':
                print("Allah bless you.")
            elif hru == "not good":
                print("I'm so sorry.")

        elif "bye" in command:
            print(f'{ai}: {aft}\n{ai}: Good bye.')
            press = input(f'{ai}: Press "enter" to exit: ')
            if press == "":
                break
        else:
            query = command
            print('Searching...')
            try:
                results = wikipedia.summary(query, sentences=2)
                print('Got it.')
                print('According to Wikipedia - ')
                print(results)
            except:
                print(f"{ai}: I didn't get that!")
                print("Try it yourself.")
                webbrowser.open('www.google.com')
        print(f'Next command {user}.')


def verification():
    ##################################
    # Verification
    ##################################
    admin = "mamun"
    pswrd = "mamun"
    adask = input("Verification--\nUsername: ").lower()
    psask = input("Password: ")
    if adask == admin:
        if psask == pswrd:
            print(f"{ai}: Oh! {user}")
            greet_me()
            print(f"{ai}: Hello {user}, how can I help you?")
            main()
        else:
            print(f"{ai}: Sorry! I can't give you any accesses.")
    else:
        print(f"{ai}: Sorry! I can't give you any accesses.")


if __name__ == "__main__":
    verification()
