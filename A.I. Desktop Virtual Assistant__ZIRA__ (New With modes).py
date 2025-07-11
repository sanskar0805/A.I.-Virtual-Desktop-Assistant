import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser as wb
import random
import os 
import smtplib
import platform
import wmi
import pyjokes
import time
import requests
import socket
import pywhatkit as pwk # Check this out in pypi.org
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Enter your name here so that i can call you with that name.")
myName = input("Enter your name : ")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning  {myName}.")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {myName}.")

    else:
        speak(f"Good evening {myName}.")

    print("How can i help you ?")
    speak("This is Zira . How can I help you ?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source: # Remember take device index for your mic. If not known then write this command: print(sr.Microphone.list_microphone_names())
        print("Listening....")
        r.pause_threshold = 1 # To know more about threshhold press ctrl key and click on pause_threshold
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print("Sorry Can't recognize you. Can you please say it again.")
        speak("Sorry Can't recognize you. Can you please say it again.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("Please enter your email address and password for logging in...")
    server.login(input("Enter your email address : "), input("Enter your email password: "))
    speak("Enter your email address for sending the mail...")
    server.sendmail(input("Please enter your email address again: "), to, content)
    server.close()
    speak("Email has been sent to the receiver!")

def confEmail():
    a = takeCommand()
    if a == "yes":
        sendEmail(to, content)

    elif a=="no":
        speak("Then enter what to write in the email ")
        c = input("Enter what to write in the email: \n")
        sendEmail(to, c)

def feeling_bored():
    speak("Do you want to listen some jokes or some music ?")
    print("say I want some jokes if you want to listen jokes or say I want music for music else say no")
    b = takeCommand()
    if b == "I want jokes":
        speak("Here is the joke that i found ?")
        jo = pyjokes.get_joke(language='en', category='all')
        print(jo)
        speak(jo)

    elif b == "I want music":
        print('Playing songs on groove music...')
        speak('Playing songs on groove music...')
        path = 'D:\\Gaana\\Favourite songs'
        song = os.listdir(path)
        rand_No = random.randint(0, 55)
        os.startfile(os.path.join(path, song[rand_No]))


if __name__ == "__main__":
    wishMe()
    print("I have 4 different modes for you to work with me.")
    speak("I have 4 different modes for you to work with me. They are as follows:")
    print("\t Modes \t\t How to activate ?\n", "\tApp mode (You can open specific apps in this mode.)", "\t\tSay \"open apps\" or \"applications\"\n",
    "\toffice mode", "\t\tSay \"open office\"\n", "\tWeb mode", "\t\tJust say \"web\"\n", "\tfeelings mode", "\t\tJust say \"feelings\"\n", "To change between the modes you have to first say \"exit\" to exit from the last mode.")
    time.sleep(5)
    
    while True:
        query = takeCommand().lower()

        if "hello" in query:
            print("Hi ! What i can do for you ?")
            speak("Hi ! What i can do for you ?")

        elif 'email' in query:
            try:
                speak("Enter the email address of your receiver: ")
                to = input("Enter the email address of your receiver: ")
                speak("what to write in the in the email")
                content = takeCommand()
                print(content)
                speak(f"{content}, This is your content ")
                speak("Is it correct say yes or no")
                confEmail()
            
            except Exception as e:
                print(f"Sorry, I am unable to send the mail due to an error",
                       {e})
                speak("Sorry! I am unable to send the mail due to an error, Try solving the error.")

        elif "whatsapp message" in query or "message":
            pwk.sendwhatmsg(str(input("Enter the mobile number of the receiver: ")), str(input("Enter the message to be sent : \n")), int(input("Enter the time hour: ")), "\n", int(input("Enter the minutes: ")), "\n", int(input("Enter the wait time (in sec.): ")), "\n", True)

        elif "on youtube" in query or "in youtube" in query: 
            if "in" in a:
                replaced = a.replace("play ", "")
                replaced2 = replaced.replace(" in ", "")
                replaced3 = replaced2.replace("youtube", "")
                print(f"In YouTube: {replaced3}")

            elif "on" in a:
                replaced = a.replace("play ", "")
                replaced2 = replaced.replace(" on ", "")
                replaced3 = replaced2.replace("youtube", "")
                print(f"In YouTube: {replaced3}")
        
        elif "applications" in query or "apps" in query:
            print("Which app to open ?")
            speak("Which app to open ?")
            while True:
                inquery1 = takeCommand().lower()
                print(f"User said: {inquery1}\n")
                if 'youtube' in inquery1:
                    print("opening youtube...")
                    speak('opening youtube')
                    wb.open('https://www.youtube.com/')

                elif 'gmail' in inquery1:
                    print('opening gmail')
                    speak('opening gmail')
                    wb.open('https://mail.google.com/mail/u/0/#inbox')

                elif 'visual studio code' in inquery1 or 'code' in inquery1:
                    print("Opening visual studio code...")
                    speak("Opening visual studio code...")
                    code_path = "D:\\Installed PROGRAMS\\VS code\\Microsoft VS Code\\Code.exe"
                    os.startfile(code_path)

                elif 'powershell' in inquery1:
                    print("Opening PowerShell window here...")
                    speak("Opening PowerShell window (here)...")
                    path = '"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"'
                    os.startfile(path)

                elif 'browser' in inquery1:
                    print("Opening Edge Browser... ")
                    speak("Opening Edge browser....")
                    browser_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
                    os.startfile(browser_path)
                    time.sleep(3)

                elif 'notepad' in inquery1:
                    print('Opening notepad')
                    speak('Opening notepad')
                    os.system('Notepad')
                    time.sleep(3)

                elif "exit" in inquery1:
                    print("Exiting this mode")
                    speak("Exiting this mode")
                    break

                else:
                    print("Sorry, I am not equipped to open that ! May be you are in different mode please exit that by saying exit.")
                    speak("Sorry, I am not equipped to open that ! May be you are in different mode please exit that by saying exit.")

        elif "office applications" in query or "office" in query:
            print("What to open in office ?")
            speak("What to open in office ?")
            while True:
                inquery2 = takeCommand().lower()
                print(f"User said: {inquery2}\n")
                if 'word' in inquery2:
                    print("Opening Microsoft word")
                    speak("Opening Microsoft word")
                    os.system('start winword')
                    time.sleep(3)

                elif 'excel' in inquery2:
                    print("Opening Microsoft excel")
                    speak("Opening Microsoft excel")
                    os.system('start Excel')
                    time.sleep(3)

                elif 'powerpoint' in inquery2:
                    print("Opening Microsoft powerpoint")
                    speak("Opening Microsoft powerpoint")
                    os.system('start powerpnt')
                    time.sleep(3)

                elif 'exit' in inquery2:
                    print("Exiting this mode")
                    speak("Exiting this mode")
                    break

                else:
                    print("Sorry I am unable to do that. Please try saying word, powerpoint etc. May be you are in different mode please exit that by saying exit.")
                    speak("Sorry I am unable to do that. Please try saying word, powerpoint etc. May be you are in different mode please exit that by saying exit.")

        elif 'web' in query:
            print("Tell me what to search for ?")
            speak("Tell me what to search for ?")
            while True:
                inquery3 = takeCommand().lower()
                print(f"User said: {inquery3}\n")
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    try:
                        query = query.replace("wikipedia", "")
                        results = wiki.summary(query, sentences=2)
                        speak("According to wikipedia ")
                        print(results)
                        speak(results)
                        
                    except Exception as e:
                        print(f"Sorry, I am unable to complete wikipedia search  due to this error: {e}\n Please try solving the error.")
                        speak("Sorry, I am unable to complete the wikipedia search due to an error; Please try solving the error.")
                        continue

                elif 'search' in query:
                    print("Please tell what to search on web ?")
                    speak("Please tell what to search on web ?")
                    a = takeCommand()
                    speak("Opening web search...")
                    pwk.search(a)

                elif 'website' in query or 'site' in query:
                    speak("Please enter the url of the website here")
                    try:
                        a = input("Enter the url of the website (For ex. www.youtube.com): ")
                        speak(f"Opening {a}")
                        wb.open(a)
                        time.sleep(3)

                    except Exception as e:
                        print(f"Unable to open the website due to this error {e} \n Please try to solve the error.")
                        speak("Unable to open the website due to the error. Please try to solve the error")
                        continue

                elif 'exit' in inquery3:
                    print("Exiting this mode")
                    speak("Exiting this mode")
                    break

                else:
                    print("Sorry i am unable to search for or there is an error, Please check your words. May be you are in different mode please exit that by saying exit.")
                    speak("Sorry i am unable to search for or there is an error, Please check your words. May be you are in different mode please exit that by saying exit.")

        elif 'feelings' in query:
            print("How you are feeling ?")
            speak("How you are feeling ?")
            while True:
                inquery4 = takeCommand()
                print(f"User said: {inquery4}\n")
                if 'bored' in inquery4:
                    feeling_bored()

                elif 'exit' in inquery4:
                    print("Exiting this mode")
                    speak("Exiting this mode")
                    break
                
                else:
                    print("Sorry, i am not equipped to solve you with your feeling. May be you are in different mode please exit that by saying exit.")
                    speak("Sorry, i am not equipped to solve you with your feeling. May be you are in different mode please exit that by saying exit.")

        elif 'my name' in query:
            print(f"Your name is {myName}")
            speak(f"Your name is {myName}")

        elif 'system' in query:
            print("Below are the information about your os...")
            speak("Below are the information about your operating system..")
            mysystem = platform.uname()
            print(f"System: {mysystem.system}")
            print(f"Node Name: {mysystem.node}")
            print(f"Release: {mysystem.release}")
            print(f"Version: {mysystem.version}")
            print(f"Machine: {mysystem.machine}")
            print(f"Processor: {mysystem.processor}")
            time.sleep(5)

        elif 'machine' in query:
            print("Below are the information about your machine....")
            speak("Below are the information about your machine....")
            c = wmi.WMI()   
            myMachine = c.Win32_ComputerSystem()[0]
            print(f"Manufacturer: {myMachine.Manufacturer}")
            print(f"Model: {myMachine. Model}")
            print(f"Name: {myMachine.Name}")
            print(f"NumberOfProcessors: {myMachine.NumberOfProcessors}")
            print(f"SystemFamily: {myMachine.SystemFamily}")
            time.sleep(5)

        elif 'ip' in query:
            public_ip = requests.get("https://api.ipify.org").text
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"Your public ip address is {public_ip} and your device host name is {hostname} with a local ip {local_ip}")
            speak("Your public ip address is..... and your device host name is.... with a local ip....")
            time.sleep(5)

        elif 'joke' in query:
            speak("Here is the joke that i found ?")
            jo = pyjokes.get_joke(language='en', category='all')
            print(jo)
            speak(jo)

        elif 'play music' and 'play songs' in query or 'song' in query:
            try:
                print('Playing songs on groove music...')
                speak('Playing songs on groove music...')
                path = 'D:\\Gaana\\Favourite songs'
                song = os.listdir(path)
                rand_No = random.randint(0, 55)
                os.startfile(os.path.join(path, song[rand_No]))

            except Exception as e:
                print(f"Sorry ! {myName}, I am unable to play songs due to the following error\n{e}")

        elif 'date' in query or 'time' in query:
            current_time = datetime.datetime.now().strftime("%A, %d %B, %Y  %H:%M:%S")
            print(f"Today's day date and time is {current_time}")
            speak(f"Today's day date and time is {current_time}")

        elif 'shutdown' in query:
            print('Shutting down this pc...')
            speak('Shutting down this pc...')
            os.system("shutdown /s /t 0")
            exit()

        elif 'restart' in query:
            print("Restarting this pc...")
            speak("Restarting this pc...")
            os.system("shutdown /r /t 0")
            exit()

        elif 'quit' in query or 'exit' in query:
            print("Thanks for interacting with me. Have a energetic and wonderful day.")
            speak("Thanks for interacting with me. Have a energetic and wonderful day.")
            exit()

        elif 'how are you' in query:
            print("I am fine and what about you ?")
            speak("I am fine and what about you ?")
            a = takeCommand()
            if a == "I am fine":
                print("Ok, That's great.")
                speak("Ok, That's great.")

        else: 
            print("Sorry, but for the time being. I am not equipped to do that.")
            speak("Sorry, but for the time being. I am not equipped to do that.")
