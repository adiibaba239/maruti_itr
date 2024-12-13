# speech_handler.py

import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import subprocess
import json

def speak(text, language='en'):
    if language == 'en':
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        tts = gTTS(text, lang=language)
        tts.save("temp.mp3")
        subprocess.Popen(["start", "temp.mp3"], shell=True)
"""
import os
import pygame
import time
from gtts import gTTS
from pydub import AudioSegment
import tempfile

def change_pitch(audio_path, output_path, semitones=2):
    sound = AudioSegment.from_mp3(audio_path)
    sound_with_altered_pitch = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (semitones / 12.0)))
    })
    sound_with_altered_pitch.export(output_path, format="mp3")

def speak(song_lyrics, slow=True, male_voice=True):
    try:
        # Create a gTTS object with the song lyrics
        singing_performance = gTTS(text=song_lyrics, lang='en', slow=slow)

        # Save the singing performance as an audio file in a temporary directory
        temp_dir = tempfile.gettempdir()
        output_file = os.path.join(temp_dir, "singing_performance.mp3")
        singing_performance.save(output_file)

        if male_voice:
            # Change pitch to make the voice sound more like a male
            changed_pitch_output = os.path.join(temp_dir, "male_voice_singing_performance.mp3")
            change_pitch(output_file, changed_pitch_output, semitones=3)
            output_file = changed_pitch_output

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load(output_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Get the actual duration of the audio file
        audio_duration = len(AudioSegment.from_file(output_file)) / 1000  # Convert milliseconds to seconds

        # Wait for the singing to finish
        time.sleep(audio_duration)

    except Exception as e:
        print(f"Error during singing performance: {str(e)}")

# Example usage with direct text input:
"""

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='en-IN').lower()
        print(f"Command recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
