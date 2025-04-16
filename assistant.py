# thư viện pyttsx3 chuyển văn bản thành giọng nói
# pip install pyttsx3 and pip install pywin32 
import pyttsx3
import datetime
import webbrowser as wb
import os
import time
import requests
# Nhận diện giọng nói
# pip install SpeechRecognition
# pip install pyaudio
import speech_recognition as sr
import winsound  
import random

# Khởi tạo pyttsx3
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

# Hàm phát âm thanh
def speak(audio):
    print('Trợ lý: ' + audio)
    friday.say(audio)
    friday.runAndWait()

# Hàm lấy thời gian hiện tại
def current_time():
    Time = datetime.datetime.now().strftime('%I:%M:%p')
    speak(Time)

# Chào người dùng
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Chào buổi sáng")
    elif hour >= 12 and hour < 18:
        speak("Chào buổi chiều")
    if hour >= 18 and hour < 24:
        speak("Chào buổi tối")
    speak("Tôi có thể giúp gì cho bạn?")

# Hàm nhận lệnh bằng giọng nói
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='vi-VN')
        print("Người dùng: " + query)
    except sr.UnknownValueError:
        query = str(input('Lệnh của bạn là:'))
    return query.lower()

# Hàm đặt báo thức
def set_alarm():
    speak("Bạn muốn đặt báo thức vào lúc mấy giờ?")
    alarm_time = command()
    alarm_time = ''.join(filter(str.isdigit, alarm_time))  # Lấy chỉ số từ chuỗi
    alarm_time = alarm_time[:2] + ":" + alarm_time[2:]  # Thêm dấu ":" giữa giờ và phút
    alarm_time = alarm_time + " AM"  # Giả sử bạn đặt PM mặc định
    
    speak(f"Đặt báo thức vào lúc {alarm_time}")
    # Chuyển đổi thời gian báo thức sang định dạng 24h
    alarm_time = datetime.datetime.strptime(alarm_time, '%I:%M %p').time()
    
    # Kiểm tra mỗi phút
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            speak("Đến giờ rồi! Dậy đi!")
            winsound.Beep(1000, 1000)  
            break
        time.sleep(60)  # Kiểm tra mỗi phút

# Hàm lấy thông tin thời tiết
def get_weather():
    speak("Bạn muốn xem thời tiết ở thành phố nào?")
    city = command()
    
    # Thay API Key và endpoint phù hợp
    api_key = "bf4bfca38a51bd6178217f4e22c83a60"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data['cod'] == 200:
        main = weather_data['main']
        temp = main['temp']
        weather = weather_data['weather'][0]['description']
        speak(f"Thời tiết ở {city} là {weather} với nhiệt độ {temp}°C.")
    else:
        speak("Xin lỗi, tôi không thể lấy thông tin thời tiết cho thành phố đó.")

# Hàm tìm kiếm Google
def search_google():
    speak("Bạn muốn tìm kiếm gì trên Google?")
    search = command()
    url = f"https://www.google.com/search?q={search}"
    wb.get().open(url)
    speak(f"Đây là kết quả tìm kiếm của bạn cho {search} trên Google.")

# Hàm tìm kiếm YouTube
def search_youtube():
    speak("Bạn muốn tìm kiếm gì trên YouTube?")
    search = command()
    url = f"https://www.youtube.com/search?q={search}"
    wb.get().open(url)
    speak(f"Đây là kết quả tìm kiếm của bạn cho {search} trên YouTube.")

# Hàm mở video YouTube
def open_video():
    video = f"https://www.youtube.com/watch?v=DKEzJ2_lUjk"
    os.startfile(video)

# Hàm mở website
def open_website():
    website = f"https://tuanflute275.site/"
    os.startfile(website)

# Hàm phát nhạc
def play_music():
    speak("Bạn muốn nghe bài hát gì?")
    song = command()  # Nhận tên bài hát từ người dùng

    # Tạo danh sách các URL video YouTube
    music_urls = {
        "nơi này có anh": "https://www.youtube.com/watch?v=FN7ALfpGxiI",  # Shape of You
        "lạc trôi": "https://www.youtube.com/watch?v=Llw9Q6akRo4",  # Blinding Lights
        "đừng làm trái tim anh đau": "https://www.youtube.com/watch?v=BiQBL3-DVTI&list=RDBiQBL3-DVTI&start_radio=1",  # Stay
    }

    # Kiểm tra xem bài hát người dùng yêu cầu có trong danh sách không
    if song.lower() in music_urls:
        song_url = music_urls[song.lower()]
        wb.get().open(song_url)
        speak(f"Đang phát bài {song} trên YouTube.")
    else:
        speak(f"Xin lỗi, tôi không có bài {song} trong danh sách nhạc.")

# Hàm mở ứng dụng
def open_application():
    speak("Bạn muốn mở ứng dụng nào?")
    app_name = command()
    apps = {
        "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "word": "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE",
        "notepad": "C:/Windows/system32/notepad.exe",
        "excel": "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE",
        "powerpoint": "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE", 
        "máy tính": "C:/Windows/System32/calc.exe",  
        "đồng hồ": "C:/Windows/System32/timedate.cpl",  
        "paint": "C:/Windows/System32/mspmsnsv.exe", 
        "máy ảnh": "start microsoft.windows.camera:",
    }
    if app_name in apps:
        if app_name == "máy ảnh":
            os.system(apps[app_name]) 
        else:
            os.startfile(apps[app_name])
        
        speak(f"Đang mở {app_name}.")
    else:
        speak(f"Xin lỗi, tôi không biết cách mở {app_name}.")

# Chào hỏi
def greeting(query):
    if "hello" in query or "xin chào" in query:
        speak("Chào bạn, tôi có thể giúp gì cho bạn?")
    elif "khỏe không" in query or "bạn có khỏe không" in query:
        speak("Tôi khỏe, cảm ơn bạn! Còn bạn thì sao?")
    elif "hôm nay thế nào" in query:
        speak("Tôi rất ổn, cảm ơn bạn đã hỏi!")
    elif "công việc của bạn" in query:
        speak("Tôi đang làm việc chăm chỉ để giúp bạn. Còn bạn thì sao?")
    elif "bạn đang làm gì" in query:
        speak("Tôi đang chờ bạn ra lệnh. Bạn có cần giúp đỡ gì không?")
    elif "chào buổi sáng" in query:
        speak("Chào buổi sáng! Bạn có kế hoạch gì trong ngày hôm nay không?")
    elif "chào buổi tối" in query:
        speak("Chào buổi tối! Hôm nay của bạn thế nào?")
    elif "bạn là ai" in query or "ai vậy" in query:
        speak("Tôi là một trợ lý ảo, được xây dựng bởi TUANFLUTE275. Tôi có thể giúp bạn làm rất nhiều việc!")
    elif "bạn có thể làm gì" in query:
        speak("Tôi có thể giúp bạn kiểm tra thời gian, thời tiết, mở ứng dụng, tìm kiếm trên Google và YouTube, và nhiều việc khác!")
    elif "mấy giờ rồi" in query:
        current_time()
    elif "hôm nay là ngày gì" in query:
        day_of_week = datetime.datetime.now().strftime('%A')
        speak(f"Hôm nay là {day_of_week}.")
    else:
        speak("Tôi không hiểu lắm câu hỏi của bạn, bạn có thể nói lại không?")
       
# chơi game
def guessing_game():
    number = random.randint(1, 10)
    speak("Hãy đoán một số từ 1 đến 10!")

    spoken_number = command().lower()  
    vietnamese_numbers = {
        "một": 1,
        "hai": 2,
        "ba": 3,
        "bốn": 4,
        "năm": 5,
        "sáu": 6,
        "bảy": 7,
        "tám": 8,
        "chín": 9,
        "mười": 10,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10
    }

    guess = vietnamese_numbers.get(spoken_number)

    if guess is None:
        speak("Xin lỗi, tôi không hiểu bạn nói số mấy. Bạn hãy thử lại.")
        return

    if guess == number:
        speak("Chúc mừng, bạn đoán đúng!")
    else:
        speak(f"Rất tiếc, số đúng là {number}. Thử lại nhé!")

if __name__ == "__main__":
    welcome()
    while True:
        query = command()
        if "thời gian" in query:
            current_time()
        elif "báo thức" in query:
            set_alarm()
        elif "thời tiết" in query:
            get_weather()
        elif "google" in query:
            search_google()
        elif "youtube" in query:
            search_youtube()
        elif "video của tôi" in query:
            open_video()
        elif "website của tôi" in query:
            open_website()
        elif "nhạc" in query:
            play_music()
        elif "mở" in query:
            open_application()
        elif "chơi game" in query:
            guessing_game()
        else:
            greeting(query)  
