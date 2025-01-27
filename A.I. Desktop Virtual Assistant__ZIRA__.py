import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia as wiki
import webbrowser as wb
import random, os, smtplib, platform, wmi, pyjokes, time, requests, socket
import pywhatkit as pwk
import time
import re


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
    print("\nYou can ask 'what i can say' ?")


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
        query.replace('zira', '')
        
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
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query.
        if "hello" in query:
            print("Hi ! How can i help you ?")
            speak("Hi ! How can i help you ?")

        elif 'say' in query or 'ask' in query:
            print("You can say.......")
            speak("You can say.....")
            print("open youtube","\n",
            "open google","\n",
            "Send email","\n",
            "You can also ask for any wikipedia, for ex. India Wikipedia","\n",
            "print current date and time ?","\n",
            "Play songs or Play music","\n",
            "Print machine information","\n",
            "Print system properties")
            speak("open youtube...! Or open google...! Or...Send email; For information You can ask for any wikipedia; ! Or.. print current date and time ?...! Also You can say Play songs or Play music... ; For your machine you can say print machine information also you can say print system properties for system information.")
            time.sleep(3.5)

        elif 'wikipedia' in query:
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

        elif 'open youtube' in query:
            print("opening youtube...")
            speak('opening youtube')
            wb.open('https://www.youtube.com/')

        #used the re module to replace multiple words at a single time by using less lines and codes
        elif "on youtube" in query or "in youtube" in query: 
            yt = re.sub(r'\b(youtube|on youtube|in youtube)\b', '', query)
            print(f"Playing {yt} on YouTube")
            time.sleep(1)
            pwk.playonyt(yt)

        #used the re module to replace multiple words at a single time by using less lines and codes
        elif 'search' in query or 'web' in query or 'google' in query:
            yt = re.sub(r'\b(search|search on google|on web|in web|on google|in google)\b', '', query)
            speak("On web....")
            pwk.search(query)
        
        elif 'open google' in query:
            print("opening google on web...")
            speak('opening google on web...')
            wb.open('https://www.google.com/webhp')
             
        elif 'open stack overflow' in query or 'open stackoverflow' in query:
            print("opening stackoverflow...")
            speak('opening stackoverflow in browser')
            wb.open('https://stackoverflow.com/questions/tagged/python')

        elif 'open gmail' in query:
            print('opening gmail')
            speak('opening gmail')
            wb.open('https://mail.google.com/mail/u/0/#inbox')

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
            
        #Now songs will be played on youtube as per your needs
        elif 'play music' and 'play songs' in query or 'song' in query or 'play song' in query or 'music' in query:
            try:
                time.sleep(1)
                print("Which song do you want to play?")
                speak("Which song do you want to play?")
                q1 = takeCommand().lower()
                if 'any' in q1:
                    s1 = re.sub(r'\b(on youtube|in youtube| on web|)\b', '', q1)
                    my_list = ["https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL15B1E77BB5708555", "https://www.youtube.com/watch?v=U0ZoqmyGJo8&ab_channel=MelodyChillMix", "https://www.youtube.com/watch?v=nFgsBxw-zWQ&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa", "https://www.youtube.com/watch?v=ugeRr5HbsU4&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D"]
                    random_choice = random.choice(my_list)
                    print("Playing song on YT....")
                    speak("Playing song on youtube....")
                    wb.open_new(random_choice)
                
                else:
                    s2 = re.sub(r'\b(youtube|on youtube|in youtube)\b', '', q1)
                    print("Playing song on YT.....")
                    speak("Playing song on youtube .....")
                    time.sleep(1)
                    pwk.playonyt(s2)

            except Exception as e:
                print(f"Sorry ! {myName}, I am unable to play songs due to the following error\n{e}")
                continue

        elif 'date' in query or 'time' in query:
            current_time = datetime.datetime.now().strftime("%A, %d %B, %Y  %H:%M:%S")
            print(f"Today's day date and time is {current_time}")
            speak(f"Today's day date and time is {current_time}")
        
        elif 'visual studio code' in query or 'code' in query:
            print("Opening visual studio code...")
            speak("Opening visual studio code...")
            code_path = "D:\\Installed PROGRAMS\\VS code\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'powershell' in query:
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
                print(content)
                speak(f"{content}, This is your content ")
                speak("Is it correct say yes or no")
                confEmail()
            
            except Exception as e:
                print(f"Sorry, I am unable to send the mail due to an error",
                       {e})
                speak("Sorry! I am unable to send the mail due to an error, Try solving the error.")

        elif "whatsapp message" in query or "message" in query:
            pwk.sendwhatmsg(str(input("Enter the mobile number of the receiver with country code (+91): ")), 
            str(input("Enter the message to be sent : \n")), int(input("Enter the time hour: ")), 
            int(input("Enter the minutes: ")), int(input("Enter the wait time (2<)")), True)

        elif 'my name' in query:
            print(f"Your name is {myName}")
            speak(f"Your name is {myName}")

        elif 'browser' in query:
            print("Opening Edge Browser... ")
            speak("Opening Edge browser....")
            browser_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(browser_path)
            time.sleep(3)
        
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

        elif 'thank you' in query:
            print("Your most welcome !  You can ask me anything, anytime and anywhere. See you soon...")
            speak("Your most welcome !  You can ask me anything, anytime and anywhere. See you soon...")
            print("Should I leave ? Say Yes or No.")
            speak("Should I leave ? Say Yes or No.")
            a = takeCommand()
            if a == "yes" or a == "Yes":
                speak("Ok. See you soon. Bye!")
                exit()
            else:
                continue

        elif 'joke' in query:
            speak("Here is the joke that i found ?")
            jo = pyjokes.get_joke(language='en', category='all')
            print(jo)
            speak(jo)

        elif 'bored' in query:
            feeling_bored()

        elif 'ip' in query:
            public_ip = requests.get("https://api.ipify.org").text
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"Your public ip address is {public_ip} and your device host name is {hostname} with a local ip {local_ip}")
            speak("Your public ip address is..... and your device host name is.... with a local ip....")
            time.sleep(5)

        elif 'notepad' in query:
            print('Opening notepad')
            speak('Opening notepad')
            os.system('Notepad')
            time.sleep(3)

        elif 'word' in query:
            print("Opening Microsoft word")
            speak("Opening Microsoft word")
            os.system('start winword')
            time.sleep(3)

        elif 'excel' in query:
            print("Opening Microsoft excel")
            speak("Opening Microsoft excel")
            os.system('start Excel')
            time.sleep(3)

        elif 'powerpoint' in query:
            print("Opening Microsoft powerpoint")
            speak("Opening Microsoft powerpoint")
            os.system('start powerpnt')
            time.sleep(3)

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
            print("Thanks for interacting with me. Have a good day.")
            speak("Thanks for interacting with me. Have a good day.")            
            exit()
            
        else: 
            False
