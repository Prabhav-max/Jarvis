import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
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
if __name__ == "__main__":
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