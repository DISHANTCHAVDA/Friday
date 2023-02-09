# Documented by DISHANT CHAVDA
import time
import psutil
import pyttsx3  # pip install pyttsx3 (For Speak)
import datetime
import speech_recognition as sr
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import pyjokes  # pip install pyjokes
import os
import pyautogui  # pip install pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha  # pip install wolframalpha

engine = pyttsx3.init()
wolframalpha_app_id = 'PEQ8T3-TYLPJYP2LK'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")  # for 24 hour clock
    speak("the current time is")
    speak(Time)
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # for 12-hour clock
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back DISHANT Sir")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("GOOD MORNING,DISHANT SIR!!")
    elif 12 <= hour < 18:
        speak("GOOD AFTERNOON DISHANT SIR!!")
    elif 18 <= hour < 24:
        speak("GOOD EVENING DISHANT SIR!!")
    else:
        speak("GOOD NIGHT DISHANT SIR!!")
    speak("Friday AT YOUR SERVICE, I'M ONLINE AND READY!!!")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Friday is Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)

    except Exception as e:
        print(e)
        print("Pardon me sir, could you repeat that")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('cybersecdc@gmail.com', 'securityby367!')
    server.sendmail('cybersecdc@gmail.com', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)


def joke():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/DC/PycharmProjects/firstpProg/My Personal Assistant.png')


if __name__ == '__main__':

    wishme()

    while True:
        query = TakeCommand().lower()
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        if 'time' in query:
            time_()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = TakeCommand()
                # provide_receiver_email_address
                # Receiver = 'reciever_is_Sleepandmakemoneyy@gmail.com'
                receiver = input("Enter Receiver Email address")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak("Unable to send email.")

        elif 'search in brave' in query:
            speak('What you would like to search Sir...?')
            bravepath = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            search = TakeCommand().lower()
            wb.get(bravepath).open_new_tab(search)

        elif 'search in youtube' in query:
            speak('What you would like to search in youtube Sir')
            search_Term = TakeCommand().lower()
            speak('here we go Sir we are in youtube window')
            wb.open('https://www.youtube.com/results?search_query=' + search_Term)

        elif 'search in google' in query:
            speak('What you would like to search in google Sir?')
            search_Term = TakeCommand().lower()
            speak('Searching on google')
            wb.open('https://www.google.com/search?q=' + search_Term)

        elif 'play a song online' in query:
            speak('What you would like to listen Sir')
            search_Term = TakeCommand().lower()
            speak('here we go Sir we are in wink music as i find it first on google')
            wb.open('https://wynk.in/music/detailsearch/' + search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak("Going offline Sir!!")
            quit()

        elif 'hello' in query:
            speak("hello sir, what can i do for you!!!")

        elif 'how are you' in query:
            speak("im fine sir, thank you for asking, how about you Sir!, what can i do for you!!")

        elif 'vs code' in query:
            speak("Opening VS code sir!!")
            vs_code = r"C:\Users\DC\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(vs_code)

        elif 'take a note' in query:
            speak('what you want to write in note, sir??')
            notes = TakeCommand()
            file = open("notes.txt", 'w')
            speak('Sir should i include Date and time??')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("note has been successfully written and saved,Sir")
            else:
                file.write(notes)

        elif 'show my notes' in query:
            speak('showing notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()
            speak("screenshot has been successfully Saved, here is your screenshot sir")
            ss = r"C:\Users\DC\PycharmProjects\firstpProg\My Personal Assistant.png"
            os.startfile(ss)

        elif 'good morning' in query:
            gm_dir = 'C:/Users/DC/PycharmProjects/firstpProg/My Personal Assistant/Songs/4.mp3'
            os.startfile(gm_dir)

        elif 'play song offline' in query:
            songs_dir = 'C:/Users/DC/PycharmProjects/firstpProg/My Personal Assistant/Songs/'
            music = os.listdir(songs_dir)
            speak('What you would like to listen Sir')
            speak('select a number')
            ans = TakeCommand().lower()
            while 'number' not in ans and ans != 'random' and ans != 'you choose':
                speak('''i couldn't understand you, please try again sir''')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1, 100)
            os.startfile(os.path.join(songs_dir, music[no]))

        elif 'can you remember' in query:
            speak("Sure Sir!!, Go ahead i will remember")
            memory = TakeCommand()
            speak("You asked me to remember that" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'thanks' in query:
            speak("Your most welcome sir,     jarvis is online and ready at your service any time")
            quit()

        elif 'thank you' in query:
            speak("Your most welcome sir,     jarvis is online and ready at your service any time")
            quit()

        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("you asked me to remember that your name is" + memory)

        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0f60fb12059c4550a56918e913628bbe''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news')
                print('''=============== TOP HEADLINES ============''' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('THE ANSWER IS: ' + answer)
            speak('The answer is' + answer + "sir")

        elif 'sleep' in query:
            speak('For How many second you want me to sleep sir??')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)
            speak('im back sir, online and ready')

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
