import random
import time
import tkinter as tk
from gtts import gTTS
import pygame
import os

# List of colors in Spanish with corresponding RGB values
colors = {
    "violeta": "#8A2BE2",  # Violet
    "verde": "#008000",    # Green
    "gris": "#C0C0C0", # Silver
    "azul": "#0000FF",     # Blue
    "rosa": "#FFC0CB"      # Pink
}

# Initialize pygame mixer for playing audio
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Fullscreen mode
root.configure(bg="black")

# Label to display color name
label = tk.Label(root, text="", font=("Arial", 80), fg="white", bg="black")
label.pack(expand=True)

def speak_and_display_color():
    """Chooses a random color, speaks it in Spanish, and updates the screen."""
    color_name = random.choice(list(colors.keys()))
    color_hex = colors[color_name]

    # Speak the color using gTTS
    print(color_name)
    tts = gTTS(text=color_name, lang='es')
    tts.save("color.mp3")
    pygame.mixer.music.load("color.mp3")
    pygame.mixer.music.play()

    # Update screen background and text
    root.configure(bg=color_hex)
    label.config(text=color_name.upper(), bg=color_hex)

    # Show the color for 3 seconds, then change
    root.after(1500, speak_and_display_color)

# Start displaying colors
speak_and_display_color()

# Quit the program when "Escape" is pressed
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()

# Clean up the audio file after program exits
if os.path.exists("color.mp3"):
    os.remove("color.mp3")
