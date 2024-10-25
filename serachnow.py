import pyttsx3  
import speech_recognition as sr
from playsound import playsound
import pywhatkit
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hey, say something...")
        playsound("./sounds/activate.wav") # Fixed typo here: "energy_thresold" to "energy_threshold"
        audio = recorder.listen(source, 0, 5)
    
    try:
        query = recorder.recognize_google(audio, language='en-IN')
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    

    
def searchGooglee(query):
    if "google" in query:
        import wikipedia as googleScrap
        query=query.replace("bestie"," ")
        query=query.replace("on google"," ")
        query=query.replace("google"," ")
        speak("This is what i found on google")
        try:
            pywhatkit.search(query)
            result= googleScrap.summary(query,1)
            speak(result)
        except:
            speak("no speakable output available")

def searchYoutube(query):
    if "youtube" in query.lower():
        speak("this is what i found on youtube")

        pywhatkit.playonyt(query)
        speak(f"Done,bestie")
        
def searchWikipedia(query):
    if "wikipedia" in query.lower():
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia","")
        query=query.replace("search wikipedia","")
        query= query.replace("bestie","")
        results= wikipedia.summary(query,sentences=2)
        speak("according to wikipedia..")
        print(results)
        speak(results)
            