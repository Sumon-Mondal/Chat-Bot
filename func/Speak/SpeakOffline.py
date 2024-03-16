#pip install pyttsx3
import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)


def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
    print(Fore.CYAN+audio)
    engine.say(audio)
    engine.runAndWait()
