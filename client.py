import requests
import speech_recognition as sr
from gtts import gTTS
import os
import time


# Function to record audio
def record_audio(recognizer, microphone, timeout_duration):
    with microphone as source:
        print("Говорите")
        try:
            audio = recognizer.listen(source, timeout=timeout_duration)
            return audio
        except sr.WaitTimeoutError:
            print("Пользователь ничего не сказал в течение времени ожидания")
            return None

# Function to recognize speech
def recognize_speech(recognizer, audio):
    try:
        message_txt = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + message_txt)
        return message_txt
    except sr.UnknownValueError:
        print("Не удалось распознать")
        return None
    except sr.RequestError:
        print("Не получилось запросить результаты")
        return None

def text_to_speech(text, lang='ru'):

    tts = gTTS(text, lang=lang)

    tts.save("output.mp3")

    os.system("mpg321 output.mp3") # Use 'mpg321' to play the audio


# Main function to send request
def send_request(user_content):
    url = "http://194.59.40.99:7990/process_text/"
    system_content = "Вы умная колонка, созданная Шамилем. Отвечай на русском языке."

    payload = {"system_content": system_content, "user_content": user_content}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    message_txt = response.json()["response"]
    print(message_txt)
    time.sleep(1)

    text_to_speech(message_txt)

# Main code
if __name__ == "__main__":
    mic = sr.Microphone()
    r = sr.Recognizer()

    audio = record_audio(r, mic, timeout_duration=5)
    if audio is not None:
        user_content = recognize_speech(r, audio)
        if user_content:
            send_request(user_content)