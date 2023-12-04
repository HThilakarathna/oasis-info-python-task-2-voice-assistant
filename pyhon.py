import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None

# Function to perform basic tasks based on user commands
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What would you like me to search for?")
        search_query = recognize_speech()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")

    else:
        speak("I'm sorry, I don't understand that command.")

# Main loop
while True:
    user_command = recognize_speech()
    if user_command:
        process_command(user_command)
