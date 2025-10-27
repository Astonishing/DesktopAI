import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can change voice later
    engine.setProperty('rate', 175)  # Speaking speed
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello Abdul, Jarvis online and ready for commands.")
