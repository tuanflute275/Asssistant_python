# thư viện pyttsx3 chuyển văn bản thành giọng nói
# pip install pyttsx3 and pip install pywin32 
import pyttsx3
# thư viện datetime có sẵn của python 
import datetime
# Mở link
import webbrowser as wb 
# os
import os
# Nhận diện giọng nói
# pip install SpeechRecognition
# pip install pyaudio
# import speech_recognition as sr

friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print('Assistant : ' + audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    Time=datetime.datetime.now().strftime('%I:%M:%p')
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    if hour >= 18 and hour < 24:
        speak("Good Night")
    speak("How Can I Help You ?")

def command():
    # c=sr.Recognition()
    # with sr.Microphone() as source:
    #     c.pause_threshold=2
    #     audio=c.listene(source)
    # try:
    #     query=c.recognize_google(audio, language='en')
    #     print("Tuan Flute: "+ query)
    # except sr.UnknownValueError:
    #     query=str(input('Your order is:'))
    query=str(input('Your order is:'))
    return query    
    
if __name__ == "__main__":
    welcome()
    while True:
        query=command().lower() # lấy mệnh lệnh về chữ thường
        if "google" in query:
            speak("Searching...")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("Searching...")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        if "open video" in query:
            video=f"https://youtu.be/iaSXi2jhjo8?si=7jY-JaFX5SUuJzZe"
            os.startfile(video)
        if "open website" in query:
            website=f"https://tuanflute275.site/"
            os.startfile(website)
        if "time" in query:
            time()