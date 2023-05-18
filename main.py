import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import openai
from gnewsclient import gnewsclient
from playsound import playsound
import datetime
client = gnewsclient.NewsClient(language='english',location='india',max_results=3)
import time
import wmi
from selenium import webdriver
from utils import websites
import pyjokes
from urllib.request import urlopen
import json
from ecapture import ecapture as ec
import requests
import getpass

def say(text):
    text_to_speech = pyttsx3.init()
    text_to_speech.say(text)
    text_to_speech.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Unable to Recognizing your voice.")  
        return "None"
    return query

def takeCommanduser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Name of User or Group")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'Client to whome message is to be sent is : {query}\n')

    except Exception as e:
        print (e)
        print("Unable to recognize Client name")
        say("Unable to recognize Client Name")
        print("Check your Internet Connectivity")
    return query

def takeCommandmessage():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Enter Your Message")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'Message to be sent is : {query}\n')

    except Exception as e:
        print (e)
        print("Unable to recognize your message")
        print("Check your Internet Connectivity")
    return query


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
        #print("Listning...")
        query= takeCommand()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                # say(query)
        

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

        if "calculate" in query:
            query = query.replace(" ","")
            query = query.replace("calculate","")
            query = query.replace("evaluate","")
            if 'into' in query:
                query = query.replace("into","*")
            if 'by' in query:
                query = query.replace("by","/")
            try:
                result=eval(query)
            except:
                result="invalid"
            print("The result is: ",str(result))
            say("Result is "+str(result))
        
        if "send a whatsaap message" in query or "send a WhatsApp message" in query:
            driver = webdriver.Chrome('Web Driver Location')
            driver.get('https://web.whatsapp.com/')
            say("Scan QR code before proceding")
            tim=10
            time.sleep(tim)
            say("Enter Name of Group or User")
            name = takeCommanduser()
            say("Enter Your Message")
            msg = takeCommandmessage()
            count = 1
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
            msg_box = driver.find_element_by_class_name('_3u328')
            for i in range(count):
                msg_box.send_keys(msg)
                button = driver.find_element_by_class_name('_3M-N-')
                button.click()
        if 'how are you' in query:
            say("I am fine , Thank you")
            say("How are you??")
        
        if 'joke' in query:
            say(pyjokes.get_joke())

        if 'is love' in query:
            say("It is 7th sense that destroy all other senses")
                
        if "who are you" in query:
            say("I am your virtual assistant created by Tyflon")

        if "will you be my girlfriend" in query or "will you be my boyfriend" in query:  
            say("I'm not sure about , may be you should give me some time")

        if "how are you" in query:
            say("I'm fine, glad you asked me that")

        if "i love you".lower() in query:
            say("It's hard to understand")

        if "open Gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
        if "where is" in query:
            query=query.replace("where is","")
            location = query
            say("Locating ")
            say(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        
        if "bye" in query:
            print("Adios amigose")
            say("Adios amigose")
            exit(0)