# importing modules
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib

# setting Engine to pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# defining the speak() function, this will recognize and the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# defining the greet() function, this will greet the indivudial and also term something about itself
def greet():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am MCA, a virtual voice asssitant based on Python. \n")
    speak("I am MCA, a virtual voice assistant based on Python.")

# defining the username() function, this will ask the user for their name, register it and say it back as a welcoming message
def username():
    print("What should I call you .?\n")
    speak("What should i call you ?")
    name = command()
    
    print(" Welcome ", name, "\n")
    
    speak("Welcome")
    speak(name)
    
    print("How May I Help You...? \n")
    speak("How May I Help You ?")

# defining the command() function, this will enable the user to give out commands, it will recognize the given commands and thus function accordingly
def command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening. Speak Now.")
        print("\nListening... \n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Understanding your command ")
        print("Understanding... \n")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception as e:
        print(e)
        speak("Sorry.. I am having trouble understanding. Please Repeat") 
        print("Could not Understand Command... \n")
        speak("You can try greeting me with hello or any navigation commands. Or you can try a wikipedia search. I can also send a desired email.") 
        return "None"

    return query

# defining the sendEmail() function, this will enable the use of SMTP
def sendEmail(mail, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'Your-password')
    server.sendmail('', mail, content)
    server.close()

# calling every function into our main() function and defining some functionality attributes to registered commands
if __name__ == "__main__":
    
    clear = lambda: os.system('cls')

    clear()
    greet()
    username()

    while True:
        query = command().lower()

        if 'hello' in query or 'hi' in query or 'what are you' in query or 'hai' in query:
            speak("Hello.  I am the  METICULOUS   COMPLAISANT   ASSISTANT    A K A  MCA.  I have been made to  perform some pre defined tasks  and thus establish the semi automation of your PC.")

        elif 'who designed you' in query or 'who made you' in query:
            speak("I have been designed by Shantanu and Rohit to automate Personal Computers. But like all of us, I am also a work in progress")

        elif 'tell me a joke' in query or 'joke' in query:
            result = pyjokes.get_joke()
            speak("Here's a joke for you")
            print(result)
            speak(result)

        elif 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak('Searching Wikipedia')
            speak("Fetching Results for" + query)
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'open stack overflow' in query:
            speak("Directing to stackoverflow.com")
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query or 'play songs' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            speak("Opening Music")
            speak("Playing Now, Make You Mine")
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open photos' in query:
            photo_dir = 'C:\\Users\\hurtl\\Desktop\\MY INTEL\\02.03.20'
            photo = os.listdir(photo_dir)
            speak("Opening Your Favorite Photos")
            # print(photo)
            os.startfile(os.path.join(photo_dir, photo[0]))
            

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The Current IST time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            speak("Opening  Visual Studio Code")
            os.startfile(codePath)

        elif 'email to me' in query:
            
            try:
                speak("What should I send?")
                content = command()
                speak("To whom shall i send this mail ?")
                mail = command()
                sendEmail(mail, content)
                speak("Your message has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this mail")

        elif 'cbit' in query or 'go to cbit' in query:
            speak("Directing to CBIT")
            webbrowser.open("https://cbit.ac.in")

        elif 'student login' in query:
            speak("Directing to CBIT Student Login")
            webbrowser.open("https://erp.cbit.org.in")

        elif 'shutdown system' in query:
            speak("Hold on. Confirm shutdown ? ")
            print("Confirm Shutdown (Yes/No)?")

            choice = command()
            
            if 'confirm' in choice or 'yeah' in choice:
                speak("Shutting Down Now")
                print("Shutting Down...")
                subprocess.call('shutdown [/f] [/p] ')                   # not working, system error
            elif 'no' in choice:
                speak('Got it. Uncommencing shutdown.')
                print("System Shutdown  Uncommenced...")

        elif 'exit' in query or 'stop' in query:
            print('Commencing Exit Sequence Now\n')
            speak("Alright Then. Bye bye.  Have a Great Time.")
            print('Commenced Exit Sequence \n')
            print("\n\nGoodBye :)")
            exit()
            
