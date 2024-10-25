import wolframalpha
import pyttsx3
import speech_recognition

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wolfram_query(query):
    apikey = "JP7954-AJWEWGG2PG"
    client = wolframalpha.Client(apikey)
    try:
        response = client.query(query)
        answer = next(response.results).text
        return answer
    except Exception as e:
        print(f"Error: {e}")
        return None
def calc(query):
    modified_query = query.replace("bestie", "")
    modified_query = modified_query.replace("multiply", "*")
    modified_query = modified_query.replace("plus", "+")
    modified_query = modified_query.replace("minus", "-")
    modified_query = modified_query.replace("divide", "/")

    result = wolfram_query(modified_query)
    if result:
        speak(f"The result is {result}")
        print(f"The result is {result}")
    else:
        speak("Sorry, I couldn't perform the calculation.")
        