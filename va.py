import speech_recognition as sr
import pyttsx3 as tts
from datetime import datetime
import webbrowser
import time
r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak('ask')
        audio = r.listen(source)
        voice = ''
    try:
        voice = r.recognize_google(audio, language="tr")
    except sr.UnknownValueError:
        speak("I don't understand.")
    except sr.ReferenceError:
        speak("System is not working.")

    return voice


def response(voice):
    if 'nasılsın' in voice:
        speak("thanks sir. I am good!")
    if 'Hey tisa' in voice:
        speak("Yes sir!")
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        speak("what do you want to search sir?")
        search = record()
        webbrowser.open('https://google.com/search?g='+search)
        speak('what i found for'+search)
    if 'çal' in voice:
        speak("okey sir. what would you like to listen to?")
        search = record()
        webbrowser.open('https://www.youtube.com/results?search_query='+search)

    if 'tamamdır' in voice:
        speak('See you later sir!')
        exit()


def speak(string):
    tts.speak(string)


speak("Hello sir, How can I help you?")
time.sleep(1)
while(1):
    ses = record()
    print(ses)
    response(ses)
