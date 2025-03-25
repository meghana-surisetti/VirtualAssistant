import speech_recognition as sr
import pywhatkit as pwt
import pyautogui as pg
import webbrowser
import calendar as c
import pyttsx3
import time as t
import tkinter as tk
from tkinter import *
from GoogleNews import GoogleNews
pyobj=pyttsx3.init()
r = sr.Recognizer()
print('yes boss '+'i am your assistant'+' tell me boss')
pyobj.say('yesboss'+'i am your assistant'+'tell me boss')
pyobj.say("how can i help you")
pyobj.runAndWait()
pyobj.stop()
def listen():
    try:
        with sr.Microphone() as source:
            print("YOU CAN SPEAK NOW!")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print("you said:{}".format(text))
            if "audio" in r.recognize_google(audio):
                fo=open("C:\\Users\\meghana\\OneDrive\\Desktop\\read1.txt","r",encoding="utf-8")
                new=fo.read()
                pyobj.say(new)
                pyobj.runAndWait()
            elif "calendar" in r.recognize_google(audio):
                pyobj.say("text")

                print(c.calendar(2023))
            elif "time" in r.recognize_google(audio):
                pyobj.say("text")
                dc = Tk()
                dc.title("digital clock")
                dc.geometry("650x100")
                def time():
                    d = t.strftime("%d-%m-%Y,%H:%M:%S")
                    l.config(text=d)
                    l.after(60,time)
                l = Label(dc,font=("Arial",40),bg="black",fg="blue")
                l.pack()
                time()
                mainloop()
            elif "news" in r.recognize_google(audio):
                pyobj.say("text")
                googlenews = GoogleNews()
                googlenews = GoogleNews(period = '7d')
                googlenews.search('india')
                result = googlenews.result()
                for x in result:
                    print("-"*50)
                    print("Title--",x['title'])
                    print("Date/time--",x['date'])
                    print("Description--",x['desc'])
                    print("Link--",x['link'])
            elif "search" in r.recognize_google(audio):
                pyobj.say(text)
                pwt.search(text)
                pyobj.say("your search is successful")
                pyobj.runAndWait()
            elif "play" in r.recognize_google(audio):
                pyobj.say(text)
                pwt.playonyt(text)
                pyobj.say("yes! working on it")
                pyobj.runAndWait()
            elif "message" in r.recognize_google(audio):
                pwt.sendwhatmsg("+918074202982","hello people!",14,47)
                pg.press("enter")
            elif "group" in r.recognize_google(audio):
                pwt.sendwhatmsg_to_group("LPbxHL4r1I02gm7ry17wFq", "Hey Guys! How's everybody?", 14,52)
    except:
        print("could not recognize your voice")
listen()