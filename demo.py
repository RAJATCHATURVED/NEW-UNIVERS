import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0 ].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour>=12:
        speak("GOOD MORNING!")  

    elif hour>=12 and hour<18:
        speak("GOOD Afternoon!=")

    else:
        speak("Good Evening!")  


    speak("i am javas sir.please teel me how may i help you")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
  
    try:
        
       print("Recognizing..")
       query = r.recognize_google(audio,Language='en-in')
       print(f"user said: {query}\n")

    except Exception as e:
      
       print("say that again please..") 
       return "None"    
    return query

if __name__=="__main__": 
   wishme()
  
   takecommand()
   while True:
     query = takecommand().lower()

     if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query. replace("wikipedia", "")
          results = wikipedia. summary (query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

     elif 'open youtube' in query:
          webbrowser .open ("youtube.com")

     elif 'open google' in query:
          webbrowser .open ("google.com")

     elif 'open stackoverflow'in query:
           webbrowser.open("stackoverflow.com")
