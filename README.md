### Code Description
This Python script is a simple Text to Morse Code Converter with an interactive graphical user interface (GUI) built using tkinter. It allows users to input text, convert it to Morse code, play the Morse code as audio, and also decode Morse code back to text. Here's a breakdown of the main components:

1. **Audio Setup**:
   - The script uses Pygame to handle audio playback for Morse code signals.
   - Two audio files (`long.wav` and `short.wav`) are loaded for the long and short Morse code signals respectively.
   - Error handling ensures that the audio files exist before proceeding.

2. **Morse Code Dictionary**:
   - Morse code mappings are stored in a dictionary (`MORSE_CODE_DICT`), which is created by reading from a CSV file (`morse_code.csv`).
   - The CSV file contains mappings of characters to their corresponding Morse code symbols.

3. **Function Setup**:
   - `clear_text`: Clears the text and Morse code widgets when clicked or when any key is pressed.
   - `text_to_morse`: Converts input text to Morse code and updates the Morse code display.
   - `morse_to_text`: Converts Morse code input to text and updates the text display.
   - `play_morse_audio`: Plays the Morse code audio based on the Morse code input.

4. **UI Setup**:
   - The tkinter GUI is created with various widgets:
     - Labels for displaying Morse code mappings.
     - Text widget for inputting text to convert to Morse code.
     - Text widget for displaying Morse code input or decoding results.
     - Button for playing the Morse code audio.

### ABOUT CODE
---
# Text to Morse Code Converter

This Python script provides a simple GUI-based Text to Morse Code Converter. It allows users to input text, convert it to Morse code, play the Morse code as audio, and also decode Morse code back to text.

### Features:
- Convert text to Morse code.
- Decode Morse code to text.
- Play Morse code as audio.
- Interactive graphical user interface (GUI) using tkinter.
- Audio playback using Pygame.

### Setup Instructions:
1. Make sure you have Python installed on your system.
2. Install the required dependencies:
   ```
   pip install pandas pygame
   ```
3. Clone this repository or download the `morse_code_converter.py` script.

### Usage:
1. Run the script:
   ```
   python morse_code_converter.py
   ```
2. The GUI window will appear with the following components:
   - Labels displaying Morse code mappings.
   - Text area to input text for encoding.
   - Text area to input Morse code for decoding.
   - Play button to play the Morse code audio.

### How to Use:
- **Encoding Text to Morse Code:**
  1. Click on the text area labeled "Click Here and Insert Text to Encode".
  2. Input your desired text.
  3. The corresponding Morse code will be displayed in the lower text area.

- **Decoding Morse Code to Text:**
  1. Click on the text area labeled "Enter Morse Code to Decode Separated by Space".
  2. Input the Morse code separated by spaces.
  3. The decoded text will be displayed in the upper text area.

- **Playing Morse Code as Audio:**
  1. After entering Morse code to decode, click the "Play" button.
  2. The Morse code will be played as audio, with short and long signals represented by different tones.

### Note:
- Ensure that the audio files `long.wav` and `short.wav` are in the `assets/` directory.
- If these files are missing, an error message will be displayed, and the script will exit.

### Contributors:
- WLQ innovations

### License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

For any issues or suggestions, please feel free to open an [issue](https://github.com/your/repository/issues). We welcome contributions!