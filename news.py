import requests
import json
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=fa99b5e0fb9c4468895f939baf247f0f",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=fa99b5e0fb9c4468895f939baf247f0f",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=fa99b5e0fb9c4468895f939baf247f0f",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=fa99b5e0fb9c4468895f939baf247f0f",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=fa99b5e0fb9c4468895f939baf247f0f"
    }
    
    url = None
    speak("Which field of news do you want: [business], [health], [technology], [entertainment]?")
    field = input("Type field news that you want: ")

    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("URL was found")
            break

    if url is None:  # No valid URL was found
        print("URL not found")
        return  # Exit the function if no valid URL

    try:
        news = requests.get(url).text
        news = json.loads(news)
        speak("Here is the news")
        
        arts = news["articles"]
        for article in arts:
            title = article["title"]
            print(title)
            speak(title)
            news_url = article["url"]
            print(f"For more info visit: {news_url}")
            
            a = input("[Press 1 to continue] and [Press 2 to stop]: ")
            if str(a) == "2":
                break
        speak("That's all")
        
    except Exception as e:
        print("An error occurred:", e)
        speak("Sorry, I couldn't fetch the news.")

