import pyttsx3  
import datetime

engine =   pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak(f"Good Morning,bestie")
    elif hour>12 and hour<=15:
        speak(f"Good Afternoon,bestie")
    else:
        speak(f"Good Evening,bestie")
    speak("Please tell me, How can i assist you?")
    