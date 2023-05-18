import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import openai
from gnewsclient import gnewsclient
from playsound import playsound
import datetime
client = gnewsclient.NewsClient(language='english',location='india',max_results=3)

def say(text):
    text_to_speech = pyttsx3.init()
    text_to_speech.say(text)
    text_to_speech.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"User Said: {query}")
            say(query)
            return query
        except Exception as e:
            return "Some error Occured Sorry from Neom"

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning")

    elif hour>=12 and hour<18:
        say("Good Afternoon")

    else:
        say("Good Evening")

    say("Why to fear if neom is here")

if __name__ == '__main__':
    # say("Hello I am NEOM")
    wish()
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

        if "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S") 
            say(f"The time is {strftime}")

        if "news" in query:
            news_list = client.get_news()
            for item in news_list:
                st = item['title'].split(' - ', 1)[0]
                print(st)
                say(st)
        if "suggest" in query:
            query = query.replace("suggest", "best")
            query = query.replace(" ","+")
            webbrowser.open("www.google.com/search?q="+query)
            say("These are some results")

        