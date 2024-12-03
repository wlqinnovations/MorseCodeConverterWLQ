import pandas as pd
from tkinter import *
import pygame
import os

# ---------------------------- Audio Set Up --------------------------- #
# File path to audio
long_audio = "assets/long.wav"
short_audio = "assets/short.wav"

# Initialize Pygame mixer
pygame.mixer.init()

# Load audio files
if os.path.exists(long_audio) and os.path.exists(short_audio):
    long_sound = pygame.mixer.Sound(long_audio)
    short_sound = pygame.mixer.Sound(short_audio)
else:
    long_sound = short_sound = None

# ---------------------------- Morse Code Dict ------------------------ #
# Read CSV with Morse code alphabet
df = pd.read_csv("morse_code.csv")
MORSE_CODE_DICT = {row.character: row.morse_code for (_, row) in df.iterrows()}

# ---------------------------- FUNCTION SETUP -------------------------- #
# Clear explanatory texts
def clear_text(event=None):
    global widgets_cleared
    if not widgets_cleared:
        text.delete('1.0', END)
        morse_code.delete('1.0', END)
        widgets_cleared = True

# Convert text to Morse code
def text_to_morse(event):
    input_text = event.widget.get('1.0', END).strip().upper()
    morse_code_text = ' '.join([MORSE_CODE_DICT.get(char, char) for char in input_text])
    morse_code.delete('1.0', END)
    morse_code.insert('1.0', morse_code_text)

# Normalize Morse code (replace . with • for consistency)
def normalize_morse_code(input_code):
    return input_code.replace('.', '•')

# Convert Morse code to text
def morse_to_text(event):
    morse_input = morse_code.get('1.0', END).strip()
    # Normalize Morse code (replace • with . for consistency)
    morse_input = normalize_morse_code(morse_input)
    words = morse_input.split('   ')  # Split by three spaces for word separation
    decoded_message = []
    for word in words:
        decoded_word = ''.join(
            [key for code in word.split() for key, value in MORSE_CODE_DICT.items() if value == code]
        )
        decoded_message.append(decoded_word)
    text.delete('1.0', END)
    text.insert('1.0', ' '.join(decoded_message))

# Global variable to control playback
stop_playback = False

def play_morse_audio_callback(morse_code, index=0):
    global stop_playback
    if stop_playback or index >= len(morse_code):
        return  # Stop playback or complete
    signal = morse_code[index]
    if signal in ['.', '•'] and short_sound:
        short_sound.play()
        window.after(int(short_sound.get_length() * 1000), lambda: play_morse_audio_callback(morse_code, index + 1))
    elif signal == '-' and long_sound:
        long_sound.play()
        window.after(int(long_sound.get_length() * 1000), lambda: play_morse_audio_callback(morse_code, index + 1))
    elif signal == ' ':
        window.after(500, lambda: play_morse_audio_callback(morse_code, index + 1))  # Pause between characters
    else:
        play_morse_audio_callback(morse_code, index + 1)  # Skip unrecognized characters

def play_morse_audio_button():
    global stop_playback
    stop_playback = False
    morse = morse_code.get('1.0', END).strip()
    play_morse_audio_callback(morse)

def stop_morse_audio():
    global stop_playback
    stop_playback = True
    pygame.mixer.stop()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=10, pady=10, bg='skyblue')
window.title('Text to Morse Code Converter by WLQ')
window.iconbitmap('morse-icon.ico')
window.geometry("1140x1050")  # Adjusted size to fit all elements

# Bind the function to left mouse clicks and any key presses
window.bind('<Button-1>', clear_text)
window.bind('<Key>', clear_text)

# Initialize a flag to keep track of whether the widgets have been cleared or not
widgets_cleared = False

# Create Morse code labels
morse_code_label = {}
i = 0
for char, morse in MORSE_CODE_DICT.items():
    label = Label(text=f"{char}\n{morse}", width=8, relief='solid', borderwidth=2, font=('Arial', 16), bg='#FFD699')
    label.grid(row=i // 10, column=i % 10, padx=5, pady=5)
    morse_code_label[char] = label
    i += 1

# Text input for normal text
text = Text(width=90, height=10, font=('Arial', 16))
text.grid(row=7, column=0, columnspan=10, sticky='EW', pady=10)
text.insert('1.0', 'Click Here and Insert Text to Encode')
text.bind('<KeyRelease>', text_to_morse)

# Text input for Morse code
morse_code = Text(width=90, height=10, font=('Arial', 16))
morse_code.grid(row=8, column=0, columnspan=10, sticky='EW', pady=10)
morse_code.insert('1.0', 'Enter Morse Code to Decode Separated by Space')
morse_code.bind('<KeyRelease>', morse_to_text)

# Play button
play_button = Button(text='Play', relief='solid', command=play_morse_audio_button, font=('Arial', 16))
play_button.grid(row=9, column=0, columnspan=5, sticky='EW', pady=10)

# Stop button
stop_button = Button(text='Stop', relief='solid', command=stop_morse_audio, font=('Arial', 16))
stop_button.grid(row=9, column=5, columnspan=5, sticky='EW', pady=10)

window.mainloop()
