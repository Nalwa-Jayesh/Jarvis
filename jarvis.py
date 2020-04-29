import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyowm
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir.Please tell me how may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception :
     #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nalwajayesh67@gmail.com','Ashgreninja@67')
    server.sendmail('nalwajayesh67@gmail.com',to,content)
    server.close()
num=random.randint(1,16)
ch=True
count=0 
def Weather():
    own=pyowm.OWM('fcb10f9828ef10b6bf6ea8f6b45d416d')
    location= own.weather_at_place('New Delhi')
    weather=location.get_weather()
    print(weather)
    speak(weather)
    temp=weather.get_temperature('celsius')
    for key,value in temp.items():
        x=key,value
        print(key,value)
        speak(x)
    humidity=weather.get_humidity()
    print(humidity)
    speak(f"Humidity :{humidity}\n")
   
if __name__ == "__main__":
    wishMe()
    while ch:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com") 
        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")
        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        if 'file complaint'in query:
            webbrowser.open("https://services.india.gov.in/service/detail/public-grievances-portal-pg-portal")
        elif 'play music' in query:
            music_dir='D:\\Jayesh\\Music'
            songs=os.listdir((music_dir))
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'play senorita' in query:
            music_dir='D:\\Jayesh\\Music'
            songs=os.listdir((music_dir))
            os.startfile(os.path.join(music_dir,songs[13]))
        elif 'play some music' in query:
            music_dir='D:\\Jayesh\\Music'
            songs=os.listdir((music_dir))
            os.startfile(os.path.join(music_dir,songs[num]))
        elif 'play sv' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Pkh8UtuejGw")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'weather' in query:
            Weather()
        elif 'open visual studio' in query:
            codepath="C:\\Users\\nalwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open python' in query:
            codepath="C:\\Users\\nalwa\\AppData\\Local\\Programs\\Python\\Python36-32\\pythonw.exe "
            os.startfile(codepath)
        elif 'email to jayesh' in query:
            try:
                print("What should I say ?")
                content=takeCommand()
                to="nalwajayesh67.@gmail.com"
                sendEmail(to,content)
                speak("Email send")
            except Exception as e:
                print(e)
                speak("Emai not send LOL!")
        elif 'exit' in query:
            ch=False
