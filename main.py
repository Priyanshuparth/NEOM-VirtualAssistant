import speech_recognition as sr
import os
import pyttsx3

def say(text):
    text_to_speech = pyttsx3.init()
    text_to_speech.say(text)
    text_to_speech.runAndWait()



if __name__ == '__main__':
    print('Pycham')
    say("hello everyone to python")
    