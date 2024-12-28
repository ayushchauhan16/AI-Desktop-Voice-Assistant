import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi = "98ba9b23501743a3a752e1c5b0be6a07"

def speak(text):
    engine.say( text )
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="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",)

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful virtual assistant name Thor skilled in general task like Alexa and Goggle cloud."},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message
    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Check if the request was successful
    if r.status_code == 200:
        data = r.json()  # Parse JSON response
        articles = data.get("articles", [])  # Extract the list of articles
        
        # Loop through each article and print the headline
        speak("Top News Headlines:")
        for idx, article in enumerate(articles, start=1):
            speak(f"{idx}. {article['title']}")

    else:
        # Let OpenAI handle the request
        output= aiProcess(c)
        speak(output)






if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake ord "Jarvis"
        # obtain audio from the microphone"
        r = sr.Recognizer()
       
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                 print("Listening..")
                 audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Ya")
            #Listen for command
                with sr.Microphone() as source:
                     print("Jarvis Active...")
                     audio= r.listen(source)
                     command= r.recognize_google(audio)

                     processCommand(command)




        except Exception as e:
            print("Error;{0}".format(e))
