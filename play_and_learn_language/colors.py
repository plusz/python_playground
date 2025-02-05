import pyttsx3
import random
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# List of colors
# colors = ["violet", "green", "silver", "blue", "pink"]

# List of colors in Polish
colors = ["fioletowy", "zielony", "srebrny", "niebieski", "różowy"]

# Set Polish voice (replace index if needed)
engine.setProperty('voice', "com.apple.speech.synthesis.voice.zosia")  # macOS example


# Set speech rate (optional)
engine.setProperty('rate', 150)

def speak_color():
    while True:
        color = random.choice(colors)
        print(color)  # Display the color in the console
        engine.say(color)
        engine.runAndWait()
        time.sleep(0.5)  # Pause before next color

# Run the function
speak_color()
