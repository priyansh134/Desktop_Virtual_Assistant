import pyttsx3 # Command window-pip install pyttsx3
import datetime 
import wikipedia # pip install wikipedia 
import speech_recognition as sr # pip istall speechRecgnition
import webbrowser # pip install webbrowser
import os 
eng=pyttsx3.init('sapi5')
voices=eng.getProperty('voices')
url=['https://www.youtube.com/watch?v=zM6s3JgF9_0', 'https://www.youtube.com/watch?v=2nK6WBcGPOw', 'https://www.youtube.com/watch?v=k-Py11iePeM']
eng.setProperty('voice',voices[1].id)
def speak( audio):
    eng.say(audio)
    eng.runAndWait()
    # this function wish according to the current time
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Namaste  I'm robot 2.0.Please tell me how may I help you")

    # this function take the command from the user and convert into the string
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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__=="__main__":
   
   wishme()
   # All the query which you want to exceute
   while True:
       query=takeCommand().lower()
       if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)
       elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/")
           speak("Any other query sir")
       elif 'open google' in query:
           webbrowser.open("google.com")
           speak("Any other query sir")
       elif 'open gfg' in query:
           webbrowser.open("https://www.geeksforgeeks.org/")
           speak("Any other query sir")
       elif 'open college portal' in query:
           webbrowser.open("https://webportal.jiit.ac.in/jiitwebkiosk/")
           speak("Any other query sir")
       
       elif 'the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            speak("Any other query sir")
       elif 'play paris trip song' in query:
           webbrowser.open(url[0])
           speak("Any other query sir")
       elif 'play gaddi song' in query:
           webbrowser.open(url[1])
           speak("Any other query sir")
       elif 'play obsessed song' in query:
           webbrowser.open(url[2])
           speak("Any other query sir")
       
       elif 'open chat gpt' in query:
           webbrowser.open("https://openai.com/blog/chatgpt")
           speak("Any other query sir")
       elif 'open github' in query:
           webbrowser.open("https://github.com/")
           speak("Any other query sir")
       elif 'open college website' in query:
           webbrowser.open("https://www.jiit.ac.in/")
           speak("Any other query sir")
       elif 'open whatsapp' in query:
           webbrowser.open("https://www.whatsapp.com/")
           speak("Any other query sir")

       elif 'open instagram' in query:
           webbrowser.open("https://www.instagram.com/")
           speak("Any other query sir")

       
       
       elif 'stop' in query:
        speak("OK Sir")
        break