import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<16:
        speak('good afternoon! hope youre having an amazing day.')
    else:
        speak("good evening!")
    speak('My name is Iris. I will be here to help you when you need my help. How may I help you?')

def takeCommand():
    '''
    This function is made to take microphone input from the user in order to produce an output.
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print("I am sorry i didn't understand you. Please repeat your query again.")
        return "None"
    return query


if __name__=='__main__':
    #speak("Hello, my name is Iris. How may i help you?")
    wishMe()
    while True:
        query=takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'play music' in query:
            music_dir="C:\\Users\\bhakt\\Music\\Favorite song"
            songs= os.listdir(music_dir)
            random_songs=random.choice(songs)
            print(random_songs)
            os.startfile(os.path.join(music_dir, random_songs))

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime('%H P M %M minutes %S seconds')
            print(strTime)
            speak(f'right now the time is {strTime}') 