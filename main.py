import speech_recognition as sr
import os
import pyttsx3

def say(text):
    text_to_speech = pyttsx3.init()
    text_to_speech.say(text)
    text_to_speech.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio,language="en-in")
        print(f"User Said: {query}")
        return query


if __name__ == '__main__':
    print('Pycham')
    say("hello Abhijeet hehehe")
    print("Listning...")
    text= takeCommand()
    say(text)