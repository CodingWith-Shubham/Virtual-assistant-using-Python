from playsound import playsound
import os
import sys
import webbrowser
import pyttsx3
import wolframalpha
import pyjokes
import wikipedia
import pywhatkit as pwt
import time
import pyautogui
import keyboard as k
while True:
    a = input("what you want me to do?::::")
    if a == "play music":
        playsound("C:\\vs code\\chatbot\\arcade2.mp3")
      
    if a == "open vlc media player":
        os.system("VLC media player")
        os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
    if a == "open chrome":
        os.system("Google Chrome")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    if a == "exit":
        print("Exiting my sir shubham, Have a nice day:)")
        engine = pyttsx3.init()
        engine.say("have a nice day sir shubham  nice to talk with you")
        engine.runAndWait()
        sys.exit()
    if a == "open youtube":
        webbrowser.open("youtube.com")
    if a == "create a folder in my desktop":
        a = input("Give me the name of the folder which you want to make?")
        parent_dir = "C:\\Users\\Subham\\Desktop"
        path = os.path.join(parent_dir,a)
        os.mkdir(path)
        print("your folder has been created")
    if a == "speak something for me":
        b = input("What do you want me to say , my Sir Shubham")
        engine = pyttsx3.init()
        engine.say(b)
        engine.runAndWait()
    if a == "tell me a joke":
        Myjoke = pyjokes.get_joke(language="en", category="all")
        print(Myjoke)
        engine = pyttsx3.init()
        engine.say(Myjoke)
        engine.runAndWait()
    if a == "question and answer mode":
        a = input("Enter your question ::::")
        result = wikipedia.summary(a,sentences = 2)
        print(result)
        engine = pyttsx3.init()
        engine.say(result)
        engine.runAndWait()
    if a == "send whatsapp message":
        a = input("Enter whatsapp phone number::::")
        b = input("Enter the mesage which you want to send::::")
        c = int(input("Enter the time (hours)::::"))
        d = int(input("Enter the time (minutes)::::"))
        pwt.sendwhatmsg(a,b,c,d)


    else:
        print("Done! Tell me the next command")
