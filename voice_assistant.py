# voice_assistant.py

import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        return "I didn't catch that."

def react_to_emotion(emotion):
    if "sad" in emotion:
        speak("Let me tell you a story to cheer you up...")
        # Or play music, display emoji, etc.
    elif "happy" in emotion:
        speak("That's great! I'm happy too.")
    elif "angry" in emotion:
        speak("Take a deep breath. Want to hear a joke?")
    else:
        speak("I am here with you.")

if __name__ == "__main__":
    while True:
        emotion = listen()
        react_to_emotion(emotion)
