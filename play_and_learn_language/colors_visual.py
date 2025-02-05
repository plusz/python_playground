import pyttsx3
import random
import time
import tkinter as tk

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set Polish voice (adjust as needed)
engine.setProperty('voice', "com.apple.speech.synthesis.voice.zosia")  # macOS example
engine.setProperty('rate', 150)  # Adjust speech speed

# List of colors in Polish with corresponding RGB values
colors = {
    "zielony": "#008000",     # Green
    "srebrny": "#C0C0C0",     # Silver
    "niebieski": "#0000FF",   # Blue
    "różowy": "#FFC0CB"       # Pink
}


# Create the main window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Fullscreen mode
root.configure(bg="black")

# Label to display color name
label = tk.Label(root, text="", font=("Arial", 80), fg="white", bg="black")
label.pack(expand=True)

def show_color():
    """Chooses a random color, speaks it, and updates the screen."""
    color_name = random.choice(list(colors.keys()))
    color_hex = colors[color_name]
    
    # Speak the color
    print(color_name)
    engine.say(color_name)
    engine.runAndWait()
    
    # Update screen background and text
    root.configure(bg=color_hex)
    label.config(text=color_name, bg=color_hex)
    
    # Show the color for 3 seconds, then change
    root.after(650, show_color)

# Start displaying colors
show_color()

# Quit the program when any key is pressed
root.bind("<Escape>", lambda e: root.destroy())  # Press Esc to exit
root.mainloop()
