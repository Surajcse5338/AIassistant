import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("current time is")
    speak(Time)

def date():
    date=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak("and the date is")
    speak(date)
    speak(month)
    speak(year) 

def wishme():
    speak("Welcome back Sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("Good morning sir")
    elif hour>=12 and hour <18:
        speak("Good afternoon sir")
    elif hour>=18 and hour <24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Shrikant at your service sir. Tell me what can i do ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try : 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


def senEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('prashantsrivastava876@gmail.com','prashant2')
    server.sendmail('prashantsrivastava876@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
   # wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching sir.")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result) 

        elif 'send email' in query:
            try:
                speak("what shoud i send")
                content = takeCommand()
                to = 'surajshinde231@gmail.com'
                senEmail(to, content)
                speak("done sir.")
            except Exception as e:
                print(e)
                speak("unable to send.")

        elif 'open chrome' in query:
            speak("What should I search ?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')         

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'remember that' in query:
            while True:
                speak("what should i remember ?")
                data=takeCommand()
                speak("you said me to remember"+data+"am I correct ?")
                answ=takeCommand()
                if 'yes' in answ:
                    remember = open("data.txt",'w')
                    remember.write(data)
                    speak("data remembered succesfully.")
                    remember.close()
                    break
                else:
                    speak("can you please repeat the statement.")

        elif 'stop' in query:
            speak("Exiting sir.")
            quit()

