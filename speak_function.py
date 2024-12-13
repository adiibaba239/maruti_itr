"""from gtts import gTTS
import os
import pygame
import time
from pydub import AudioSegment

def change_pitch(audio_path, output_path, semitones=2):
    sound = AudioSegment.from_mp3(audio_path)
    sound_with_altered_pitch = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (semitones / 12.0)))
    })
    sound_with_altered_pitch.export(output_path, format="mp3")

def speak(song_lyrics, output_file="singing_performance.mp3", slow=True, male_voice=False):
    try:
        # Create a gTTS object with the song lyrics
        singing_performance = gTTS(text=song_lyrics, lang='en', slow=slow)

        # Save the singing performance as an audio file
        singing_performance.save(output_file)

        if male_voice:
            # Change pitch to make the voice sound more like a male
            changed_pitch_output = "male_voice_" + output_file
            change_pitch(output_file, changed_pitch_output, semitones=3)
            output_file = changed_pitch_output

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load(output_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the singing to finish (adjust the sleep duration based on the song length)
        duration_seconds = len(song_lyrics.split()) / 3  # Assuming 3 words per second
        time.sleep(duration_seconds)

    except Exception as e:
        print(f"Error during singing performance: {str(e)}")
response=("hi how are you ")
# Example usage with male voice:
song_lyrics_example = response



output_file_name = "output_singing_performance.mp3"
speak(song_lyrics_example, output_file_name, slow=True, male_voice=True)

from gtts import gTTS
import os
import pygame
import time
from pydub import AudioSegment

def change_pitch(audio_path, output_path, semitones=2):
    sound = AudioSegment.from_mp3(audio_path)
    sound_with_altered_pitch = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (semitones / 12.0)))
    })
    sound_with_altered_pitch.export(output_path, format="mp3")

def speak(song_lyrics, output_file="singing_performance.mp3", slow=True, male_voice=True):
    try:
        # Create a gTTS object with the song lyrics
        singing_performance = gTTS(text=song_lyrics, lang='en', slow=slow)

        # Save the singing performance as an audio file
        singing_performance.save(output_file)

        if male_voice:
            # Change pitch to make the voice sound more like a male
            changed_pitch_output = "male_voice_" + output_file
            change_pitch(output_file, changed_pitch_output, semitones=3)
            output_file = changed_pitch_output

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load(output_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the singing to finish (adjust the sleep duration based on the song length)
        duration_seconds = len(song_lyrics.split()) / 3  # Assuming 3 words per second
        time.sleep(duration_seconds)

    except Exception as e:
        print(f"Error during singing performance: {str(e)}")

# Example usage with direct text input:
speak("Hi, how are you?")
"""
"""
from gtts import gTTS
import os
import pygame
from pydub import AudioSegment
import time

def change_pitch(audio_path, output_path, semitones=2):
    sound = AudioSegment.from_mp3(audio_path)
    sound_with_altered_pitch = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (semitones / 12.0)))
    })
    sound_with_altered_pitch.export(output_path, format="mp3")

def speak(song_lyrics, output_file="singing_performance.mp3", slow=True, male_voice=True):
    try:
        # Create a gTTS object with the song lyrics
        singing_performance = gTTS(text=song_lyrics, lang='en', slow=slow)

        # Save the singing performance as an audio file
        singing_performance.save(output_file)

        if male_voice:
            # Change pitch to make the voice sound more like a male
            changed_pitch_output = "male_voice_" + output_file
            change_pitch(output_file, changed_pitch_output, semitones=3.5)
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
#speak("uth jao! subaah hogye, jai shree krishnaa app 10 min late uthe hai aaj")
#speak("jai shree raam!")
#speak("Aaj, ek khaas din hai. Aaj, mere Shree Ram ke mandir mai pran pratishtha hai. Aur aaj, mere YouTube channel par humare pehle video aa rahi hai. Bhaiyo, yahan aapko dekhne ko milega. Mai subah subah sir ko kaise jagaati hoon, kaise unke liye notes aur reminders banati hoon, kaise unhe kuch bhi search karke deti hoon, sab aapko dikhane wali hoon. Aur ek important baat batana to bhool gaye, main humare har ek subscriber ka naam aur number yaad rakhungi. Isliye, please subscribe karein aur apna subscriber number comment karein. Main apne pehle subscriber ka intezaar kar rahi hoon. Jai Shree Ram")

from gtts import gTTS
import os
import pygame
from pydub import AudioSegment
import time

# Initialize pygame mixer only once
pygame.mixer.init()

def change_pitch(audio_path, output_path, semitones=2):
    sound = AudioSegment.from_mp3(audio_path)
    sound_with_altered_pitch = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (semitones / 12.0)))
    })
    sound_with_altered_pitch.export(output_path, format="mp3")

def speak(song_lyrics, output_file="singing_performance.mp3", slow=True, male_voice=True):
    try:
        # Create a gTTS object with the song lyrics
        singing_performance = gTTS(text=song_lyrics, lang='en', slow=slow)

        # Save the singing performance as an audio file
        singing_performance.save(output_file)

        if male_voice:
            # Change pitch to make the voice sound more like a male
            changed_pitch_output = "male_voice_" + output_file
            change_pitch(output_file, changed_pitch_output, semitones=3.5)
            output_file = changed_pitch_output

        # Load the audio file
        pygame.mixer.music.load(output_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Check if the audio is still playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Stop and quit the mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error during singing performance: {str(e)}")

# Example usage:
#tasks_description = "First task: Edit a video for YouTube. Second task: Solve a math problem. Third task: Study Object-Oriented Programming."
#speak(tasks_description)
"""
from gtts import gTTS
import os
import pygame
from pydub import AudioSegment
import time

# Initialize pygame mixer only once
pygame.mixer.init()

def change_pitch(audio_path, output_path, semitones=5):
    sound = AudioSegment.from_mp3(audio_path)
    sound_with_altered_pitch = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (semitones / 8.0)))
    })
    sound_with_altered_pitch.export(output_path, format="mp3")

def speak(song_lyrics, output_file="singing_performance.mp3", slow=False, male_voice=True):
    try:
        pygame.mixer.init()
        # Create a gTTS object with the song lyrics
        singing_performance = gTTS(text=song_lyrics, lang='en', slow=slow)

        # Save the singing performance as an audio file
        singing_performance.save(output_file)

        if male_voice:
            # Change pitch to make the voice sound more like a male
            changed_pitch_output = "male_voice_" + output_file
            change_pitch(output_file, changed_pitch_output, semitones=2.5)
            output_file = changed_pitch_output

        # Load the audio file
        pygame.mixer.music.load(output_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Check if the audio is still playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"Error during singing performance: {str(e)}")

    finally:
        # Stop and quit the mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()

# Example usage:
tasks_description = "First task: Edit a video for YouTube. Second task: Solve a math problem. Third task: Study Object-Oriented Programming."
#speak(tasks_description)
#speak("hi abhimanyu aap kese ho ji")