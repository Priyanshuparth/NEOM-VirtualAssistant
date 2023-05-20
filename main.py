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
import pywhatkit as kit
import os
import subprocess as sp
from config import apikey


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

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def play_on_youtube(video):
    kit.playonyt(video)


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen("C:\\Windows\\System32\\calc.exe")

def ai(prompt):
    openai.api_key = apikey
    text= f"OpenAi response for Prompt: {prompt} \n***************\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text +=response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1,235456455)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)


chatStr=""
def chat(query):
    global chatStr
    # print(chatStr)
    openai.api_key = apikey

    chatStr +=f"Tyflon: {query}\n Neom:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



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

        elif "news" in query:
            news_list = client.get_news()
            for item in news_list:
                st = item['title'].split(' - ', 1)[0]
                print(st)
                say(st)
        elif "suggest" in query:
            query = query.replace("suggest", "best")
            query = query.replace(" ","+")
            webbrowser.open("www.google.com/search?q="+query)
            say("These are some results")

        elif "calculate" in query:
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
        


        elif "send a whatsaap message" in query or "send a WhatsApp message" in query:
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
        elif 'how are you' in query:
            say("I am fine , Thank you")
            say("How are you??")
        
        elif 'joke' in query:
            say(pyjokes.get_joke())

        elif 'is love' in query:
            say("It is 7th sense that destroy all other senses")
                
        elif "who are you" in query:
            say("I am your virtual assistant created by Tyflon")

        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:  
            say("I'm not sure about , may be you should give me some time")

        elif "how are you" in query:
            say("I'm fine, glad you asked me that")

        elif "i love you".lower() in query:
            say("It's hard to understand")

        elif "open Gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
        elif "where is" in query:
            query=query.replace("where is","")
            location = query
            say("Locating ")
            say(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "open camera" in query:
            open_camera()


        elif "take a photo" in query:
            ec.capture(0,"Camera ","img.jpg")

        elif "open calculator" in query:
            open_calculator()

        elif "open command prompt" in query or "open cmd" in query:
            open_cmd()

        
        elif "write a note" in query:
            say("What should i write: ")
            note= takeCommand()
            file = open('note.txt','w')
            say("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        
        elif "show note" in query:
            say("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            say(file.read(6))

        elif "open notepad".lower() in query.lower():
                say('opening notepad for you.......')
                path = ("c:\\windows\\system32\\notepad.exe")
                os.startfile(path)

        elif "close notepad".lower() in query.lower():
                say('closing notepad wait.....')
                os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            say("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                say(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                say(" City Not Found ")

        elif "ip address".lower() in query.lower():
            say("wait")
            ip_address = find_my_ip()
            say(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.')
            print(f'Your IP Address is {ip_address}')

        elif "advice" in query:
            say(f"Here's an advice for you")
            advice = get_random_advice()
            print(advice)
            say(advice)

        elif "youtube".lower() in query.lower():
            say('What do you want to play on Youtube?')
            video = takeCommand().lower()
            play_on_youtube(video)

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)


        elif "reset chat" in query: 
            chatStr=""

        
        elif "bye" in query:
            print("Adios amigose")
            say("Adios amigose")
            exit(0)

        else:
            chat(query)