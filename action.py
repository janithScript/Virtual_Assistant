import speech_to_text
import text_to_speech
import datetime
import webbrowser
import weather


def Action(data):

    user_data = data.lower()

    if "what is your name" in user_data or "what's your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return 'My name is virtual assistant'

    elif "hello" in user_data or "hye" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("hay, sir how can i help you")
        return 'hay, sir how can i help you'
    
    elif "what you can do" in user_data or "todo" in user_data or "skills please" in user_data:
        text_to_speech.text_to_speech("you can ask anything like, time now, play music, youtube, google, chat, weather, what is your name, how are you, go0d night, good morning, bye, shutdown")
        return 'you can ask anything like, time now, play music, youtube, google, chat, weather, what is your name, how are you, good night, good morning, bye, shutdown'

    elif "how are you" in user_data or "how you" in user_data:
        text_to_speech.text_to_speech("I'm good man . Thanks for asking. ")
        return "I'm good man . Thanks for asking. "
    
    elif "bye" in user_data or "bai" in user_data:
        text_to_speech.text_to_speech("Bye my man. see you next time.")
        return "Bye my man. see you next time."

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return 'good morning sir'
    
    elif "good night" in user_data:
        text_to_speech.text_to_speech("good night sir")
        return 'good night sir.'

    elif "time now" in user_data or "time please" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okey sir")
        return 'Okey sir'

    elif "play music" in user_data:
        webbrowser.open("https://www.youtube.com/watch?v=ObQVgkdiXOU")
        text_to_speech.text_to_speech("programimg music on the way")
        return 'programimg music on the way'

    elif "youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Opening the youtube for you")
        return 'Opening the youtube for you'

    elif "google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Opening the google for you")
        return 'Opening the google for you'

    elif "chat" in user_data:
        webbrowser.open("https://chatgpt.com/")
        text_to_speech.text_to_speech("Opening chat gpt for you ")
        return 'Opening chat gpt for you '

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans


    else:
        text_to_speech.text_to_speech("sorry. I'm unable to understand")
        return "sorry. I'm unable to understand"
