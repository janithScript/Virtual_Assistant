
from logging import root
import pyttsx3
import threading
import queue
import speech_to_text
import action
from tkinter import *

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-70')
    engine.say(text)
    engine.runAndWait()

def ask():
    user_val = speech_to_text.speech_to_text()
    if user_val:
        bot_val = action.Action(user_val)
        text.insert(END, 'User--->'+ user_val+"\n")
        if bot_val:
            text.insert(END, "BOT <---"+ str(bot_val)+"\n")
        if bot_val == "Okey sir":
            root.destroy()

        # Run text_to_speech in a separate thread
        q = queue.Queue()
        t = threading.Thread(target=text_to_speech, args=(bot_val,))
        t.start()
        t.join()
