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

    speak("This is Zira . How can I help you ? If you are first time interacting me you can ask what i can say ?")
    print("\nYou can ask what i can say ?")


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
        input("Enter what to write in the email: \n")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wiki.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("opening youtube...")
            speak('opening youtube')
            wb.open('https://www.youtube.com/')

        elif 'open google' in query:
            print("opening google.com...")
            speak('opening google...')
            wb.open('https://www.google.com/webhp')
             
        elif 'open stack overflow' in query:
            print("opening stackoverflow...")
            speak('opening stackoverflow in browser')
            wb.open('https://stackoverflow.com/questions/tagged/python')

        elif 'open gmail' in query:
            print('opening gmail')
            speak('opening gmail')
            wb.open('https://mail.google.com/mail/u/0/#inbox')
        
        elif 'play music' and 'play songs' in query:
            try:
                print('Playing songs on groove music...')
                speak('Playing songs on groove music...')
                path = 'D:\\Gaana\\Favourite songs'
                song = os.listdir(path)
                print(song)
                rand_No = random.randint(0, 55)
                os.startfile(os.path.join(path, song[rand_No]))

            except Exception as e:
                print(f"Sorry ! {myName}, I am unable to play songs due to the following error\n{e}")

        elif 'current date and time' in query:
            current_time = datetime.datetime.now().strftime("%A, %d %B, %Y  %H:%M:%S")
            print(f"Today's day date and time is {current_time}")
            speak(f"Today's day date and time is {current_time}")
        
        elif 'open visual studio code' in query:
            print("Opening visual studio code...")
            speak("Opening visual studio code...")
            code_path = "D:\\Installed PROGRAMS\\VS code\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'open powershell' in query:
            print("Opening PowerShell window here...")
            speak("Opening PowerShell window (here)...")
            path = '"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"'
            os.startfile(path)

        elif 'your name' in query:
            print("Hi! My name is ZIRA. I am your A.I. virtual Desktop Assistant. How can i help you ?")
            speak("Hi! My name is ZIRA. I am your AI virtual desktop assistant. How can i help you ?")

        elif 'email' in query:
            try:
                speak("Enter the email address of your receiver: ")
                to = input("Enter the email address of your receiver: ")
                speak("what to write in the in the email")
                content = takeCommand()
                print(f"{content}, \n This is your content")
                speak(f"{content}, This is your content ")
                speak("Is it correct say yes or no")
                confEmail()
            
            except Exception as e:
                print(f"Sorry, I am unable to send the mail due to an error",
                       {e})
                speak("Sorry! I am unable to send the mail due to an error, Try solving the error.")

        elif 'say' in query:
            print("You can say.......")
            speak("You can say.....")
            print("open youtube","\n",
            "open google","\n",
            "Send email","\n",
            "You can also ask for any wikipedia, for ex. India Wikipedia","\n",
            "print current date and time ?","\n",
            "What is your name ?","\n",
            "Play songs or Play music","\n",
            "Open Powershell","\n",
            "Print machine information","\n",
            "Print system properties")
            speak("open youtube...! Or open google...! Or...Send email; For information You can ask for any wikipedia; ! Or.. print current date and time ?...! Or What is your name! Also You can say Play songs or Play music... If you are using powershell you can also say open powershell; For your machine you can say print machine information also you can say print system properties for system information.")

        elif 'quit' in query:
            print("Thanks for interacting with me. Have a energetic and wonderful day.")
            speak("Thanks for interacting with me. Have a energetic and wonderful day.")            
            exit()

        elif 'my name' in query:
            print(f"Your name is {myName}")
            speak(f"Your name is {myName}")

        elif 'browser' in query:
            print("Opening Edge Browser... ")
            speak("Opening Edge browser....")
            browser_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(browser_path)
        
        elif 'system properties' in query:
            print("Below are the information about your os...")
            speak("Below are the information about your operating system..")
            mysystem = platform.uname()
            print(f"System: {mysystem.system}")
            print(f"Node Name: {mysystem.node}")
            print(f"Release: {mysystem.release}")
            print(f"Version: {mysystem.version}")
            print(f"Machine: {mysystem.machine}")
            print(f"Processor: {mysystem.processor}")

        elif 'machine information' in query:
            print("Below are the information about your machine....")
            speak("Below are the information about your machine....")
            c = wmi.WMI()   
            myMachine = c.Win32_ComputerSystem()[0]
            print(f"Manufacturer: {myMachine.Manufacturer}")
            print(f"Model: {myMachine. Model}")
            print(f"Name: {myMachine.Name}")
            print(f"NumberOfProcessors: {myMachine.NumberOfProcessors}")
            print(f"SystemFamily: {myMachine.SystemFamily}")

        elif 'thank you' in query:
            print("Your most welcome !  You can ask me anything, anytime and anywhere.")
            speak("Your most welcome !  You can ask me anything, anytime and anywhere.")
            exit()