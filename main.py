import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import openai
from playsound import playsound

def say(text):
    text_to_speech = pyttsx3.init()
    text_to_speech.say(text)
    text_to_speech.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognixing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"User Said: {query}")
            say(query)
            return query
        except Exception as e:
            return "Some error Occured Sorry from Neom"


if __name__ == '__main__':
    say("Hello I am NEOM A.I")
    while True:
        print("Listning...")
        query= takeCommand()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                # say(query)
        if "open music" in query:
            musicPath = 'C:\\Users\\Priyanshu\\Downloads\\prop-plane-14513.mp3'
            os.system(f"open {musicPath}")