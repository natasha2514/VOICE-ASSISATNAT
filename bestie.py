import pyttsx3  
import speech_recognition as sr
from playsound import playsound
import pywhatkit
import datetime
import requests
import pyautogui
from bs4 import BeautifulSoup
import os
import speedtest
from intro import display_image
display_image("E:\\VOICE_ASSISTANT\\project\\main.png")

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def get_weather(city):
    api_key = "fcdfb8cc41f5be1095f462c6cc8dc766"  # Replace with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # "metric" for Celsius, "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        return temperature
    else:
        print("Error fetching data from OpenWeatherMap API")
        return None
    
def get_city_from_query(query):
    # Basic extraction of the city name from the query
    words = query.lower().split()
    city_index = words.index("in") + 1 if "in" in words else None
    if city_index and city_index < len(words):
        return words[city_index]
    else:
        return None
def get_ipl_score():
    try:
        from plyer import notification
        url = "https://www.cricbuzz.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # Check if any matches are listed
        teams = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
        scores = soup.find_all(class_="cb-ovr-flo")

        if len(teams) >= 2 and len(scores) >= 11:
            team1 = teams[0].get_text()
            team2 = teams[1].get_text()
            team1_score = scores[8].get_text()
            team2_score = scores[10].get_text()

            print(f"{team1} : {team1_score}")
            print(f"{team2} : {team2_score}")

            notification.notify(
                title="IPL SCORE:",
                message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
                timeout=10
            )
        else:
            print("Could not find the match details. The structure might have changed.")
            speak("I could not find the match details at the moment. Please try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("I encountered an issue while retrieving the IPL score. Please check the connection or try again later.")

speak("Whats your name?")
name=input("Type your name here:- ")
speak(f"Welcome {name}  you can activate me now...")
    
def takeCommand():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        recorder.adjust_for_ambient_noise(source, duration=1)  
        print("you can speak now...")
        playsound("./sounds/activate.wav") 
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


def alarm(a):
    timehere = open("alarmtext.txt","w")
    timehere.write(a)
    timehere.close()
    os.startfile("E:\\VOICE_ASSISTANT\\project\\alarm.py")



if __name__ == "__main__":
    while True:
        query = takeCommand()
        if query:  # Check if query is not None
            if "hey bestie" in query.lower():
                from greetme import greetMe
                greetMe()
                
                while True:
                    query = takeCommand()
                    if query:  # Check if query is not None
                        if "thank you" in query.lower():  # Fixed typo here: "thankyou" to "thank you"
                            speak(f"welcome {name} bestie! Hope I could help you")
                            break
                        elif "how are you" in query.lower():
                            speak(f"perfect,{name}")
                        elif "hello" in query.lower():
                            speak("Hello bestie, how are you?")
                        elif "apologize" in query.lower() or "say sorry" in query.lower():
                            speak(f"I am really Sorry bestie, Please forgive me {name}")
                        elif"i am fine" in query.lower():
                            speak("that's great,bestie")
                        elif "pause" in query.lower():
                            pyautogui.press("k")
                            speak(f"video paused,{name}")
                        elif"play" in query.lower():
                            pyautogui.press("k")
                            speak(f"video played,{name}")
                        elif"mute" in query.lower():
                            pyautogui.press("m")
                            speak("video muted")   
                        elif "volume up " in query.lower():
                            from keyy import volumeup
                            speak("Turning volume up")
                            volumeup()
                        elif "volume down" in query.lower():
                            from keyy import volumedown
                            speak("Turning volume down")
                            volumedown()
                        elif "open" in query.lower():
                            query= query.replace("open","")
                            query= query.replace("bestie","")
                            pyautogui.press("super")
                            pyautogui.typewrite(query)
                            pyautogui.press("enter")
                        elif "close" in query.lower():
                            from dictapp import closeappweb
                            closeappweb(query)
                        elif "google" in query.lower(): 
                            speak(f"Okay,i will bring that up on google for you,{name}")
                            pywhatkit.search(query)
                        elif"youtube" in query.lower():
                            from serachnow import searchYoutube
                            searchYoutube(query)
                        elif "wikipedia" in query.lower():
                            from serachnow import searchWikipedia
                            searchWikipedia(query)
                        elif "news" in query.lower():
                            from news import latestnews
                            latestnews()
                        elif "calculate" in query.lower():
                            from cal import wolfram_query
                            from cal import calc
                            query=query.replace("calculate","")
                            query=query.replace("bestie","")
                            calc(query)
                        elif "ipl score" in query.lower():
                            get_ipl_score()
                        elif "temperature" in query.lower() or "weather" in query.lower():
                            city = get_city_from_query(query)
                            if city:
                                temperature = get_weather(city)
                                if temperature is not None:
                                    speak(f"The current temperature in {city} is {temperature} degrees Celsius,{name}")
                                else:
                                    speak("Sorry, I couldn't retrieve the weather information at the moment.")
                            else:
                                speak("Please specify a city for the weather information.")
                        elif "set an alarm" in query.lower():
                            print("input time example:- 10 and 10 and 10")
                            speak("set the time")
                            a=input("Please tell the time :- ")
                            alarm(a)
                            speak (f"Done,{name}bestie")
                            
                        elif"internet speed" in query.lower():
                            wifi= speedtest.Speedtest()
                            upload = wifi.upload()/1048576
                            download= wifi.download()/1048576
                            print("wifi upload speed",upload)
                            print("wifi download speed",download)
                            speak(f"wifi upload speed is {upload}")
                            speak(f"wifi download speed is {download}")


                        elif "the time" in query.lower():
                            strtime= datetime.datetime.now().strftime("%H:%M")
                            speak(f"the current time is {strtime},{name}")   
                        elif "sleep" in query.lower():
                            speak(f"Okay bye! good night{name} bestie")
                            exit()
        else:
            print("No command detected, please try again.")