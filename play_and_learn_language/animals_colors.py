import random
import time
import tkinter as tk
from gtts import gTTS
import pygame
import os
from PIL import Image, ImageTk

# List of animals in Spanish with corresponding image file names
animals = {
    "lobo": "wolf.jpeg",      # Wolf
    "puma": "puma.jpeg",      # Puma
    "gato": "cat.jpeg",       # Cat
    "perro": "dog.jpeg",      # Dog
    "oso": "bear.jpeg",       # Bear
    "pato": "duck.jpeg",      # Duck
    "gallina": "hen.jpeg"     # Hen
}

# List of colors in Spanish with corresponding RGB values
colors = {
    "violeta": "#8A2BE2",  # Violet
    "verde": "#008000",    # Green
    "plateado": "#C0C0C0", # Silver
    "azul": "#0000FF",     # Blue
    "rosa": "#FFC0CB"      # Pink
}

# Initialize pygame mixer for playing audio
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Fullscreen mode
root.configure(bg="black")

# Label to display the name (color or animal)
label = tk.Label(root, text="", font=("Arial", 80), fg="white", bg="black")
label.pack(expand=True)

# Label for displaying the image of the animal
image_label = tk.Label(root)
image_label.pack(expand=True)

def speak_and_display():
    """Chooses a random color or animal, speaks its name in Spanish, and displays the result."""
    # Randomly choose between animal or color
    choice = random.choice(['animal', 'color'])
    
    if choice == 'animal':
        animal_name = random.choice(list(animals.keys()))
        image_file = animals[animal_name]

        # Speak the animal name using gTTS
        print(animal_name)
        tts = gTTS(text=animal_name, lang='es')
        tts.save("animal.mp3")
        pygame.mixer.music.load("animal.mp3")
        pygame.mixer.music.play()

        # Display the animal image
        try:
            img = Image.open(image_file)
            img = img.resize((800, 600), Image.Resampling.LANCZOS)  # Resize image to fit the screen
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img  # Keep a reference to avoid garbage collection
        except IOError:
            print(f"Image for {animal_name} not found.")
        
        # Update the label with the animal name
        label.config(text=animal_name.upper(), bg="black")

    else:  # It's a color
        color_name = random.choice(list(colors.keys()))
        color_hex = colors[color_name]

        # Speak the color name using gTTS
        print(color_name)
        tts = gTTS(text=color_name, lang='es')
        tts.save("color.mp3")
        pygame.mixer.music.load("color.mp3")
        pygame.mixer.music.play()

        # Display the color as a background
        root.configure(bg=color_hex)
        label.config(text=color_name.upper(), bg=color_hex)
        image_label.config(image='')  # Remove the animal image

    # Show the result for 3.5 seconds, then change
    root.after(1500, speak_and_display)

# Start the loop of displaying and speaking
speak_and_display()

# Quit the program when "Escape" is pressed
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()

# Clean up the audio file after the program exits
if os.path.exists("animal.mp3"):
    os.remove("animal.mp3")
if os.path.exists("color.mp3"):
    os.remove("color.mp3")
