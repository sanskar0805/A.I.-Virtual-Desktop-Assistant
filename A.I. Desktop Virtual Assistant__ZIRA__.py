import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia as wiki
import webbrowser as wb
import random, os, smtplib, pyjokes, time, requests, socket
import pywhatkit as pwk
import time
import re
import psutil, platform, wmi
import emoji


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
    print("\nYou can ask 'what i can say?'")

#Listening command by AI preparation
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
        print(f'User said: {query.replace('plus', '+')}\n')
        query.replace('zira', '')
        
    except Exception as e:
        print(e)
        print("Sorry Can't recognize you. Can you please say it again.")
        speak("Sorry Can't recognize you. Can you please say it again.")
        return "None"
    return query

#Email writing preparation
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

#feeling bored command preparation
def feeling_bored():
    speak("Do you want to listen some jokes or some music ?")
    print("say I want some jokes if you want to listen jokes or say I want music for music else say no")
    b = takeCommand().lower()
    if 'i want a joke' in b or 'i want some joke' in b or 'i want some jokes' in b or 'i want the joke' in b or 'i want the jokes' in b:
        speak("Here is the joke that i found ?")
        jo = pyjokes.get_joke(language='en', category='all')
        print(jo)
        speak(jo)

    elif "i want music" in b or "i want a music" in b or "i want a song" in b or "i want a song" in b or 'i want some music' in b or 'i want some song' in b:
        try:
                time.sleep(1)
                print("Which song do you want to play?")
                speak("Which song do you want to play?")
                q1 = takeCommand().lower()
                if 'any' in q1:
                    s1 = re.sub(r'\b(on youtube|in youtube| on web|)\b', '', q1)
                    my_list = ["https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL15B1E77BB5708555", "https://www.youtube.com/watch?v=U0ZoqmyGJo8&ab_channel=MelodyChillMix", "https://www.youtube.com/watch?v=nFgsBxw-zWQ&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa", "https://www.youtube.com/watch?v=ugeRr5HbsU4&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=eN6AYHAT8UM&ab_channel=T-Series"]
                    random_choice = random.choice(my_list)
                    print("Playing song on YT....")
                    speak("Playing song on youtube....")
                    wb.open_new(random_choice)
                
                elif 'any' in q1:
                    s2 = re.sub(r'\b(youtube|on youtube|in youtube)\b', '', q1)
                    print("Playing song on YT.....")
                    speak("Playing song on youtube .....")
                    time.sleep(1)
                    pwk.playonyt(s2)
                else:
                    takeCommand()

        except Exception as e: 
            print(f"Sorry ! {myName}, I am unable to play songs due to the following error\n{e}")
    
    else:
        b = takeCommand().lower()



#LOOP starts here... 
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query.
        if "hello" in query:
            print(emoji.emojize("       Hi !:waving_hand:  \nHow can i help you ?"))
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
            print("Responding in 5 seconds.....")
            time.sleep(5)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wiki.summary(query, sentences=3)
                speak("According to wikipedia ")
                print(results)
                speak(results)
                time.sleep(3)

            except Exception as e:
                print(f"Sorry, I am unable to complete wikipedia search  due to this error: {e}\n Please try solving the error.")
                speak("Sorry, I am unable to complete the wikipedia search due to an error; Please try solving the error.")
                continue

        elif 'news' in query or 'update me' in query or 'get me up to date' in query:
            news = ['https://www.timesofindia.indiatimes.com/','https://www.hindustantimes.com/','https://www.indianexpress.com/', 'https://www.msn.com/en-in']
            random_news = random.choice(news)
            print("Sending you to the news on web... ")
            speak("Sending you to the news on web... ")
            wb.open(random_news)
            time.sleep(3)
            input("Enter to wake up.....")

        elif 'what is the score' in query.replace("'", "") or 'whats the score' in query.replace("'", "") or 'whats the match score' in query.replace("'", "") or 'what is the match score' in query.replace("'", "") or 'what is the cricket score' in query.replace("'", "") or 'whats the cricket score' in query.replace("'", "") or 'whats the cricket update' in query.replace("'", ""):
            print("Live cricket score on web....")
            speak("Live cricket score on web....")
            wb.open('https://crex.live/')
            time.sleep(2)
            input('\nPress enter to wake up....')

        #used the re module to replace multiple words at a single time by using less lines and codes
        elif 'search' in query or 'on google' in query or 'in google' in query or 'find' in query:
            g = re.sub(r'\b(search|for|search on google|on web|in web|on google|in google|google|search for|find about|find in)\b', '', query)
            speak("On web....")
            time.sleep(1)
            pwk.search(g)
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up....")

        elif 'website' in query or 'site' in query:
            speak("Please enter the url of the website here")
            try:
                a = input("Enter the url of the website (For ex. youtube.com): ")
                speak(f"Opening {a}")
                time.sleep(1)
                wb.open(a)
                print("wait until zira responds...")
                time.sleep(5)
                input("Press enter to wake up....")
                

            except Exception as e:
                print(f"Unable to open the website due to this error {e} \n Please try to solve the error.")
                speak("Unable to open the website due to the error. Please try to solve the error")
                continue
            
        #Now songs will be played on youtube as per your needs
        elif 'play music' and 'play songs' in query or 'song' in query or 'play song' in query or 'music' in query :
            try:
                time.sleep(1)
                print("Which song do you want to play?")
                speak("Which song do you want to play?")
                q1 = takeCommand().lower()
                if 'any' in q1:
                    # we use the re module to replace the words by blank...
                    s1 = re.sub(r'\b(on youtube|in youtube| on web|)\b', '', q1)
                    my_list = ["https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL15B1E77BB5708555", "https://www.youtube.com/watch?v=U0ZoqmyGJo8&ab_channel=MelodyChillMix", "https://www.youtube.com/watch?v=nFgsBxw-zWQ&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa", "https://www.youtube.com/watch?v=ugeRr5HbsU4&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=Ps4aVpIESkc&list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK&ab_channel=T-Series", "https://www.youtube.com/watch?v=kXHiIxx2atA&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=GOkJguI8kYc&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=l75z7FrYRXI&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D"]
                    random_choice = random.choice(my_list)
                    speak("Hope you'll enjoy the song")
                    time.sleep(1)
                    print("Playing song on YT....")
                    speak("Playing song on youtube....")
                    wb.open_new(random_choice)
                    time.sleep(5)
                    input("Press enter to wake up....")
                    
                elif 'youtube' in q1 or 'play' in q1:
                    s2 = re.sub(r'\b(youtube|on youtube|in youtube)\b', '', q1)
                    speak("Hope you'll enjoy the song")
                    time.sleep(1)
                    print("Playing song on YT.....")
                    speak("Playing song on youtube .....")
                    time.sleep(1)
                    pwk.playonyt(s2)
                    time.sleep(5)
                    input("Press enter to wake up....")
                else:
                    print("Sorry Can't recognize you. Can you please say it again.")
                    speak("Sorry Can't recognize you. Can you please say it again.")
                    q1 = takeCommand().lower()

            except Exception as e:
                print(f"Sorry ! {myName}, I am unable to play songs due to the following error\n{e}")
                continue

        #used the re module to replace multiple words at a single time by using less lines and codes
        elif "on youtube" in query or "in youtube" in query or 'play' in query: 
            yt = re.sub(r'\b(youtube|on youtube|in youtube|play)\b', '', query)
            print(f"Playing {yt} on YouTube")
            speak(f"Playing {yt} on YouTube")
            pwk.playonyt(yt)
            time.sleep(5)
            input("Press enter to wake up....")

        elif 'date' in query or 'time' in query or 'day' in query:
            current_time = datetime.datetime.now().strftime(f"%A, %d %B, %Y   %H:%M:%S")
            print(f"Today's day, date and time is {current_time}")
            speak(f"Today's day, date and time is {current_time}")
            input("Press enter to wake up...")

        elif 'your name' in query:
            print("Hi! My name is ZIRA. I am your A.I. virtual Desktop Assistant. How can i help you ?")
            speak("Hi! My name is ZIRA. I am your AI virtual desktop assistant. How can i help you ?")
            time.sleep(1)

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

        elif 'remember me' in query or 'remembered me' in query:
            print(f"Yes Of course, You're {myName}")
            speak(f"Yes Of course, You're {myName}")
            time.sleep(3)

        elif 'system' in query:
            print("Below are the information about your os...")
            speak("Below are the information about your operating system..")
            mysystem = platform.uname()
            print(f"System: {mysystem.system}")
            time.sleep(1)
            print(f"Node Name: {mysystem.node}")
            time.sleep(1)
            print(f"Release: {mysystem.release}")
            time.sleep(1)
            print(f"Version: {mysystem.version}")
            time.sleep(1)
            print(f"Machine: {mysystem.machine}")
            time.sleep(1)
            print(f"Processor: {mysystem.processor}")
            time.sleep(5)
            input("Press enter to wake up...")

        elif 'machine' in query or 'configuration' in query :
            print("Below are the information about your machine....")
            speak("Below are the information about your machine....")
            # Get system information
            system_info = platform.uname()
            c = wmi.WMI()   
            myMachine = c.Win32_ComputerSystem()[0]
            # Print the system information
            # Get system information
            system_info = platform.uname()
            c = wmi.WMI()   
            myMachine = c.Win32_ComputerSystem()[0]
            # Print the system information
            print(f"Manufacturer :  {myMachine.Manufacturer}")
            time.sleep(1)
            print(f"Model        :  {myMachine. Model}")
            time.sleep(1)
            print(f"PC Name      : ", system_info.node)
            time.sleep(1)
            print(f"OS           : ", system_info.system, system_info.release)
            time.sleep(1)
            print("Version      : ", system_info.version)
            time.sleep(1)
            print("Machine Type : ", system_info.machine)
            time.sleep(1)
            print("Processor    : ", system_info.processor, f'(clock speed = {psutil.cpu_freq().max/(1000):.2f} GHz)') #2f used to print upto 2 decimal places
            time.sleep(1)
            print(f"Total RAM    :  {psutil.virtual_memory().total/(1024**3):.2f} GB")
            time.sleep(1)
            # Printing storage device
            total_space = 0
            used_space = 0
            free_space = 0

            # Get all disk partitions
            partition_space = psutil.disk_partitions()

            for part in partition_space:
                try:
                    # Usage stats
                    usage = psutil.disk_usage(part.mountpoint)
                    total_space += usage.total
                    used_space += usage.used
                    free_space += usage.free
                except PermissionError:
                    # Handle permission error
                    print(f"Permission denied for {part.device}")
                except FileNotFoundError:
                    # Handle case where mountpoint is not found
                    print(f"Mountpoint not found for {part.device}")

            # Convert bytes to gigabytes
            total_space_gb = total_space / (1024 ** 3)
            used_space_gb = used_space / (1024 ** 3)
            free_space_gb = free_space / (1024 ** 3)

            print(f"Storage device: Total space = {total_space_gb:.2f} GB, Used space = {used_space_gb:.2f} GB, Free space = {free_space_gb:.2f} GB")
            time.sleep(1)
            
            #Battery status
            battery_info = psutil.sensors_battery()

            if battery_info:
                # Calculate time left in minutes only if the battery is not plugged in
                time_left = "On power" if battery_info.power_plugged else f"{battery_info.secsleft / 60:.2f} minutes"
                
                print(f"Battery Percentage: {battery_info.percent}%, Time left: {time_left}, Power Plugged In: {'Yes' if battery_info.power_plugged else 'No'}")
            else:
                print("Battery information is unavailable...")

            time.sleep(2)
            print("Wait until ZIRA responds...")
            time.sleep(5)
            speak("Do you want to know anything else...?")
            q2 = takeCommand()
            if 'no' in q2:
                print("Ok...!")
                speak("Ok...!")
                input("Press enter to wake up....")
            else:
                continue

        elif 'hard drive' in query or 'disk' in query or 'device usage' in query or 'storage' in query:
            print("Below are the information about your connected storage device and their stats..")
            speak("Below are the information about your connected storage device and their stats..")
            # Get all disk partitions
            partition_space = psutil.disk_partitions()
            for part in partition_space:
                try:
                    # Usage stats
                    usage = psutil.disk_usage(part.mountpoint)
                    print(f"Device: {part.mountpoint}, Type: {part.fstype}, Total space: {usage.total / (1024 ** 3):.2f} GB, Space consumed: {usage.used / (1024 ** 3):.2f} GB, Space available: {usage.free / (1024 ** 3):.2f} GB")
                    time.sleep(3)
                except PermissionError:
                    # Handle permission error
                    print(f"Permission denied for {part.device}")
                except FileNotFoundError:
                    # Handle case where mountpoint is not found
                    print(f"Mountpoint not found for {part.device}")

        elif 'thank you' in query or 'thank u' in query or 'thanks' in query or 'thank' in query:
            print("Your most welcome !  You can ask me anything, anytime and anywhere. See you soon...")
            speak("Your most welcome !  You can ask me anything, anytime and anywhere. See you soon...")
            time.sleep(3)
            print("Should I leave ? Yes or No?")
            speak("Should I leave ? Yes or No?")
            a = takeCommand()
            if 'yes' in a:
                speak("Ok. See you soon. Bye!")
                exit()
            else:
                continue

        elif 'joke' in query:
            speak("Here is the joke that i found ?")
            jo = pyjokes.get_joke(language='en', category='all')
            print(jo)
            speak(jo)

        elif 'bored' in query or 'boring' in query:
            feeling_bored()

        elif 'ip' in query or 'i p' in query:
            public_ip = requests.get("https://api.ipify.org").text
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"Your public ip address is {public_ip} and your device host name is {hostname} with a local ip {local_ip}")
            speak("Your public ip address is..... and your device host name is.... with a local ip....")
            time.sleep(5)
        
        #opening web apps
        elif 'open google' in query:
            print("opening google on web...")
            speak('opening google on web...')
            wb.open('https://www.google.com/webhp')
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up....")
             
        elif 'open stack overflow' in query or 'open stackoverflow' in query:
            print("opening stackoverflow...")
            speak('opening stackoverflow in browser')
            wb.open('https://stackoverflow.com/questions/tagged/python')
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up....")

        elif 'open gmail' in query:
            print('opening Gmail')
            speak('opening gmail')
            wb.open('https://mail.google.com/mail/u/0/#inbox')
            time.sleep(3)
            input("Press enter to wake up....")

        elif 'open youtube' in query:
            print("opening YouTube...")
            speak('opening youtube')
            wb.open_new('https://www.youtube.com/')
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up....")

        elif 'whatsapp' in query:
            print("Opening WhatsApp on web...")
            speak("Opening WhatsApp on web...")
            wb.open_new_tab('https://web.whatsapp.com/')
            time.sleep(3)
            input("Press enter to wake up...")

        elif 'instagram' in query:
            print("Opening Instagram on web....")
            speak("Opening Insta on web....")
            wb.open('https://www.instagram.com/')
            time.sleep(3)
            input("Press enter to wake up...")

        elif 'facebook' in query:
            print("Opening facebook on web...")
            speak("Opening facebook on web...")
            wb.open('https://www.facebook.com/')
            time.sleep(3)
            input("Press enter to wake up...")


        #opening installed apps 
        elif 'powershell' in query or 'power shell' in query:
            print("Opening PowerShell window here...")
            speak("Opening PowerShell window (here)...")
            path = '"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"'
            os.startfile(path)
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up!..")

        elif 'command prompt' in query or 'cmd' in query:
            print("Opening command prompt...")
            speak("Opening command prompt...")
            path = '"C:\\Windows\\System32\\cmd.exe"'
            os.startfile(path)
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up...")


        elif 'visual studio code' in query or 'code' in query:
            try:
                print("Opening visual studio code...")
                speak("Opening visual studio code...")
                code_path = "D:\\Installed PROGRAMS\\VS code\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            except Exception as e:
                print(f"Sorry unable to open due to the following error\n{e}")
                speak("Sorry unable to open due to the following error")
                continue

        elif 'browser' in query or 'edge' in query:
            print("Opening Edge Browser... ")
            speak("Opening Edge browser....")
            browser_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(browser_path)
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up....")

        elif 'chrome' in query:
            try:
                # trying if chrome is installed
                print("Opening Chrome Browser....")
                speak("Opening Chrome Browser....")
                os.system('start chrome')
                print("wait until zira responds...")
                time.sleep(3)
                input("Press enter to wake up....")

            except Exception as e:
                print(f"Sorry unable to open the app due to error {e}")
                speak("Sorry unable to open the app")

        elif 'camera' in query:
            print("opening camera app...")
            speak("opening camera app...")
            os.system('start microsoft.windows.camera:')
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up...")

        elif 'notepad plus plus' in query:
            try:
                # trying if notepad ++ is installed
                print("Opening Notepad++ ....")
                speak("Opening notepad plus plus")
                os.system('start notepad++')
                time.sleep(3)
                input("Press enter to wake up....")
            except Exception as e:
                print(f"Unable to open Notepad++ due to the following error\n{e}")
                speak("Unable to open Notepad++ due to the following error")
                continue
        
        elif 'notepad' in query:
            try:
                # trying if notepad is available or not in windows
                print('Opening notepad')
                speak('Opening notepad')
                os.system('start Notepad')
                print("wait until zira responds...")
                time.sleep(3)
                input("Press enter to wake up....")
            except Exception as e:
                print(f"Sorry unable to open notepad... due to an error as follow\n{e}")
                speak("Sorry unable to open notepad... due to an error as follow")

        elif 'calculator' in query:
            print("Opening Calculator..")
            speak("Opening calculator..")
            os.system('calc')
            print("wait until zira responds...")
            input("Press enter to wake up....")

        elif 'settings' in query:
            print("Opening settings....")
            speak("Opening settings....")
            os.system('start ms-settings:')
            time.sleep(3)
            input("Press enter to wake up !")

        elif 'photos' in query:
            print("Sorry I am not equipped to do that... ")
            speak("Sorry I am not equipped to do that... ")

        elif 'explorer' in query:
            print("Opening file explorer.....")
            speak("Opening file explorer.....")
            os.system('start explorer')
            print("wait until zira responds...")
            time.sleep(3)
            input("Press enter to wake up...")

        elif 'phone link' in query:
            print("Sorry but for the time being, I am unable to do that...")
            speak("Sorry but for the time being, I am unable to do that...")

        #Opening office apps
        elif 'word' in query:
            try:
                # will try if office is installed or not...
                print("Opening MS word")
                speak("Opening MS word")
                os.system('start winword')
                print("wait until zira responds...")
                time.sleep(5)
                input("Press enter to wake up....")
            
            except Exception as e:
                print(f"Sorry, I am unable to open the app due to the following error\n{e}")
                speak("Sorry, I am unable to open the app due to the following error")
                continue

        elif 'excel' in query:
            try:
                print("Opening MS excel")
                speak("Opening MS excel")
                os.system('start Excel')
                print("wait until zira responds...")
                time.sleep(5)
                input("Press enter to wake up....")
                
            except Exception as e:
                print(f"Sorry, I am unable to open the app due to the following error\n{e}")
                speak("Sorry, I am unable to open the app due to the following error")
                continue


        elif 'powerpoint' in query:
            try:
                print("Opening MS powerpoint")
                speak("Opening MS powerpoint")
                os.system('start powerpnt')
                print("wait until zira responds...")
                time.sleep(5)
                input("Press enter to wake up....")
            
            except Exception as e:
                print(f"Sorry, I am unable to open the app due to the following error\n{e}")
                speak("Sorry, I am unable to open the app due to the following error")
                continue
            

        #System shutdown
        elif 'shutdown' in query:
            print('Shutting down this pc...')
            speak('Shutting down this pc...')
            time.sleep(1)
            os.system("shutdown /s /t 0")
            exit()

        #System Restart
        elif 'restart' in query:
            print("Restarting this pc...")
            speak("Restarting this pc...")
            time.sleep(1)
            os.system("shutdown /r /t 0")
            exit()

        #feelings 
        elif 'love you' in query or 'love u' in query:
            print(f"   (❁ ´◡`❁)\n")
            time.sleep(2)
            print(f"I love you too {myName}!\n")
            time.sleep(1)
            print("      💕")
            speak(f"I Love you Too {myName}")
            time.sleep(3)
            input("Press enter to wake up...")

        elif 'like you' in query or 'like u' in query:
            print(f"          Oh!\n")
            speak("Ohhh!\n")
            time.sleep(2)
            print("      By the way...\n")
            speak("By the way")
            print("I started liking you too!\n")
            speak(", I started liking you too!")
            print("          😻")
            time.sleep(5)
            input("Press enter to wake up...")

        elif 'whats up' in query.replace("'", ""):
            print("I am doing very great !!")
            speak("I am doing very great !!")
            time.sleep(1)
            print("How about you?")
            speak("How about you?")
            l = takeCommand()
            if 'not' in l:
                speak("Ohhh sorry to heard that from you...")
                print("Do you want to listen some music or a joke?")
                speak("Do you want to listen some music or a joke?")
                l1 = takeCommand()
                if 'music' in l1:
                    try:
                        time.sleep(1)
                        print("Which song do you want to play?")
                        speak("Which song do you want to play?")
                        q1 = takeCommand().lower()
                        if 'any' in q1:
                            s1 = re.sub(r'\b(on youtube|in youtube| on web|)\b', '', q1)
                            my_list = ["https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL15B1E77BB5708555", "https://www.youtube.com/watch?v=U0ZoqmyGJo8&ab_channel=MelodyChillMix", "https://www.youtube.com/watch?v=nFgsBxw-zWQ&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa", "https://www.youtube.com/watch?v=ugeRr5HbsU4&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=Ps4aVpIESkc&list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK&ab_channel=T-Series", "https://www.youtube.com/watch?v=kXHiIxx2atA&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=GOkJguI8kYc&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D", "https://www.youtube.com/watch?v=l75z7FrYRXI&pp=ygUNc29uZyBwbGF5bGlzdA%3D%3D"]
                            random_choice = random.choice(my_list)
                            speak("Hope you'll enjoy the song")
                            time.sleep(1)
                            print("Playing song on YT....")
                            speak("Playing song on youtube....")
                            wb.open_new(random_choice)
                            time.sleep(5)
                            input("Press enter to wake up....")
                            
                        elif 'youtube' in q1 or 'play' in q1:
                            s2 = re.sub(r'\b(youtube|on youtube|in youtube)\b', '', q1)
                            speak("Hope you'll enjoy the song")
                            time.sleep(1)
                            print("Playing song on YT.....")
                            speak("Playing song on youtube .....")
                            time.sleep(1)
                            pwk.playonyt(s2)
                            time.sleep(5)
                            input("Press enter to wake up....")
                        else:
                            print("Sorry Can't recognize you. Can you please say it again.")
                            speak("Sorry Can't recognize you. Can you please say it again.")
                            q1 = takeCommand().lower()

                    except Exception as e:
                        print(f"Sorry ! {myName}, I am unable to play songs due to the following error\n{e}")
                        continue

                elif 'joke' in l1:
                    speak("Here is the joke that i found ?")
                    jo = pyjokes.get_joke(language='en', category='all')
                    print(jo)
                    speak(jo)
                    time.sleep(2)

            elif 'good' in l or 'great' in l or 'fine' in l or 'awesome' in l:
                print("That's great to hear from you!")
                speak("That's great to hear from you!")
                time.sleep(1)

            else:
                takeCommand()

        elif 'quit' in query or 'exit' in query or 'thanks' in query or 'thank you' in query:
            print("Thanks for interacting with me. Have a good day!")
            speak("Thanks for interacting with me. Have a good day!")   
            time.sleep(2)        
            exit()
        
        elif 'pause' in query or 'stop' in query:
            print("Ok, I am Going to bed.....!\nJust wake me up whenever you want!")
            speak("Ok, I am Going to bed.....!\nJust wake me up whenever you want!")
            time.sleep(5)
            input("Press enter to wake up...!")

        elif 'open' in query:
            print("What to open?")
            speak("What to open?")
            takeCommand()


        else: 
            False
