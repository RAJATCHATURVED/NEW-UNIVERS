import os
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime


speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("hello")


say = "Hello I am muaasskaan"
speaker.Speak(say)
say = "whats your name"
speaker.Speak(say)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1

        audio = r.listen(source)
        say = "some Error Occurred. sorry from muaasskaan"
        try:
            print("recoganzging..............")
            query = r.recognize_google(audio, language="eng-in")
            print(f"user said : {query}")
            return query
        except Exception as e:
            say = "some Error Occurred. sorry from muaasskaan"
            speaker.Speak(say)

name =takeCommand()
say = f"hello {name}"
speaker.Speak(say)

if __name__ == "__main__":
    while True:
        print("Listening............")
        query = takeCommand()
        if f"search on".lower() in query.lower():
            say="what you want to search"
            speaker.Speak(say)
            query=0
            query=takeCommand()
            if query!=0:
             site=f"https://www.{query}.com"
             say = f"searching {query}"
             webbrowser.open(site)
             speaker.Speak(say)
             break

            else:
                break
        files = [["vs code", "\\Users\\sakshi\\apps\\Visual Studio Code.lnk"],
                 ["Adobe", "\\Users\\sakshi\\apps\\Adobe Acrobat.lnk"],
                 ["video editor", "\\Users\\sakshi\\apps\\NCH Suite.lnk"],
                 ["TeamViewer", "\\Users\\sakshi\\apps\\TeamViewer.lnk"],
                 ["VLC", "\\Users\\sakshi\\apps\\VLC media player.lnk"]]
        for file in files:
            if f"open {file[0]}".lower() in query.lower():
                say = f"Opening {file[0]}"
                os.startfile(file[1])
                speaker.Speak(say)

        if "how are you".lower() in query.lower():
            say = f"I am fine {name} "
            speaker.Speak(say)

        if "who created you".lower() in query.lower():
            say = f"he is a man named prratthamm joshi "
            speaker.Speak(say)

        if "fine".lower() in query.lower():
            say = f"well It is good that you are well bytheway how can I help you {name}"
            speaker.Speak(say)
        if "The time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say = f"{name} time is {hour} hours and {min} minutes"
            speaker.Speak(say)

        if "date".lower()in query.lower():
            date=datetime.date.day
            month=datetime.date.month
            say=f"{date}"
            speaker.Speak(say)