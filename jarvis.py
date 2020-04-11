import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib#Enables us to send emails using gmail

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    '''This function enables the jarvis to speak the string type audio input given to it'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function enables jarvis to greet the user'''
    hour=int(datetime.datetime.now().hour)#Returns the current hour 0-24

    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<15:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am Jarvis sir Please tell me how may I help you?')        

def takeCommand():
    '''It takes microphone input and returns string output'''
    r=sr.Recognizer()#Makes an instance of recognizer class
    with sr.Microphone() as source:#Makes microphone as a source to recognize command given int the form of speech 
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)#Stores the data in the form of audio from microphone 

    try:
        print('Recognising...')
        query=r.recognize_google(audio,language='en-in') #Converts audio data in the form of string
        print(f'User said:{query}\n') 

    except Exception as e:
        # print(e)
        print('Say that again please...')
        speak('Say that again please...')
        return 'None'
    return query  

def sendEmail(content,to):
    server=smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('something@gmail.com','password')
    server.sendmail('something@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    while True:
        wishMe() 
        query=takeCommand().lower()  

        # Logic for executing various tasks based on query 
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace('wikipedia','')#Removing wikipedia from Srk wikipedia
            results=wikipedia.summary(query,sentences=2)#Obtaining results from srk only
            speak('According to wikipedia...')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com') 

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com') 

        elif 'open google' in query:
            webbrowser.open('google.com')   

        elif 'play music' in query:
            music_dir='E:\\MyMusic' 
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f'Sir the time is {strTime}') 

        elif 'open code' in query:
            codePath="C:\\Users\\Prabhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)   

        elif 'email to prabhav' in query:
            try:
                speak('What should I say?')
                content=takeCommand()
                to='mishraprabhav8@gmail.com'
                sendEmail(content,to)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry my friend I am not able to send the mail at the moment')  

        elif 'quit' in query:
            exit()               