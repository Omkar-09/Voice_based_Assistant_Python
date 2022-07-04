from unittest import result
import webbrowser
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

rate=engine.getProperty('rate')
#print(rate)
engine.setProperty('rate',135)

volume=engine.getProperty('volume')
engine.setProperty('volume',2.0)
#print(volume)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    H=int(datetime.datetime.now().hour)
    
    if(H>=0 and H<12):talk("Good Morning Sir.")
    elif(H>=12 and H<17):talk("Good Afternoon Sir.")
    else:talk("Good Evening Sir.")
    talk('I am MARVO.......I hope your day is going well and charming...........how may i help u')
    
def listening():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Plzz command me ......I am LISTENING U CAREFULLY....")
        r.pause_threshold=0.8
        audio=r.listen(source)
    
    try:
        print("OK.....DO YOU MEAN....")
        #talk("OK.....DO YOU MEAN....")
        b=r.recognize_google(audio,language='en-in')
        print(b)
    
    except Exception as e:
        print("SORRY.......I did'nt get what u said sir")
        talk("SORRY.......I did'nt get what u said sir")
        return 'None'
    
    return b




if __name__ =="__main__":
    wish()
    while(True):
        command=listening().lower()
        
        if 'search' in command:
            talk('Searching...')
            try:
             command=command.replace('search','')
             results=wikipedia.summary(command, sentences=2)
             talk('According to wikipedia,')
             talk(results)
             print(results)
            except:
                print('Sorry i didnt got your command')
                talk('Sorry i didnt got your command')
                break

        elif 'open google' in command:
            talk("Opening")
            webbrowser.open('google.com')

        elif 'open youtube' in command:
            talk("Opening")
            webbrowser.open('youtube.com')

        elif 'open linkedin' in command:
            talk("Opening")
            webbrowser.open('linkedin.com')
        
        elif 'open github' in command:
            talk("Opening")
            webbrowser.open('github.com')

        elif 'open leetcode' in command:
            talk("Opening")
            webbrowser.open('leetcode.com')

        elif 'open instagram' in command:
            talk("Opening")
            webbrowser.open('instagram.com')
        elif 'open facebook' in command:
            talk("Opening")
            webbrowser.open('facebook.com')
        
        elif 'the time' in command:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            talk("The current time is")
            talk(time)

        elif 'hello' in command :
            print('Hello how can i helpp you ??')
            talk('hello sir, how can i help you ??')
            
        elif 'who are you' in command :
            print('I am Marvo your virtual assistant')
            talk('I am Marvo your virtual assistant. how can i help you ??')
        
        elif 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you Sir")
 
        elif 'fine' in command or "good" in command:
            talk("It's good to know that your fine")
        
        elif 'sleep' in command:
            talk("Thankyou for giving me your valuable time")
            exit()

        elif 'joke' in command:
            talk(pyjokes.get_joke())

      
        elif "write a note" in command:
            talk("What should i write, sir")
            note = listening()
            file = open('marvo.txt', 'w')
            talk("Sir, Should i include date and time")
            d = listening()
            if 'yes' in d or 'sure' in d:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in command:
            talk("Showing Notes")
            file = open("marvo.txt", "r")
            print(file.read())
            talk(file.read(6))
        
        
       

    
