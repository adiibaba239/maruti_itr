import speech_recognition as sr
import subprocess
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googletrans import Translator
from gtts import gTTS
import pyttsx3
import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import os
import time
import logging
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import platform
import pygame
import pint
ureg = pint.UnitRegistry()
import pygame.mixer
import threading
#import wikipediaapiz
import pyautogui
pygame.mixer.init()
from keywords import add_new_command_variation
from speech_handler import  listen ,speak
#from speak_function import speak1
import re
import Levenshtein
import time
import datetime
import atexit
#from face_id import capture_images
#from  kiara2 import handle_chat

from task_manager import morning_planning, add_task_by_voice, remove_task_by_voice, manage_tasks,speak_task_list,load_tasks_from_file,save_tasks_to_file,speak_tasks_by_voice
#from wishes_whatsapp import send_whatsapp_messages_to_self
tasks = load_tasks_from_file()

def preprocess_text(text):
    # Define the words to be ignored
    ignore_words = ["the", "an", "a", "in","explain", "what", "is", "purpose", "of", "concept", "how", "to", "create", "with", "html", "css"]

    # Remove unwanted characters and ignore specified words from the text
    cleaned_text = re.sub(r"[?><#!%'()_\-]", "", text)


    words = cleaned_text.split()
    filtered_words = [word.lower() for word in words if word.lower() not in ignore_words]

    result = ' '.join(filtered_words)

    return result
"""def preprocess_text(text):
    # Remove unwanted characters from the text
    cleaned_text = re.sub(r"[?><#!%'()_-]", "", text)
    return cleaned_text.lower() """


#def calculate_similarity(string1, string2):
    #return 1 - Levenshtein.distance(string1, string2) / max(len(string1), len(string2))

def preprocess_command(command):
    global command_keywords
    command_keywords = load_keywords()
    # Find the matching command based on keywords
    for key, variations in command_keywords.items():
        for variation in variations:
            if variation in command.lower():
                print(f"Match found: Key={key}, Variation={variation}, Command={command}")
                return key.lower()
    return command.lower()
def load_html_responses():
    try:
        with open('html_responses.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding HTML responses JSON: {e}")
        return []

html_responses = load_html_responses()

def load_keywords():
    try:
        with open('commands.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def click_element_with_retry(element, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            element.click()
            return True
        except ElementClickInterceptedException:
            retries += 1
            time.sleep(1)
    return False




def find_element_with_retry(driver, by, value, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            element = driver.find_element(by, value)
            return element
        except NoSuchElementException:
            retries += 1
            time.sleep(1)
    return None

def run_command(command, custom_commands, language='en'):
                processed_command = preprocess_command(command)
                recognized_command = False
               # min_similarity_threshold = .95
                if "open youtube" in processed_command:
                    webbrowser.open("https://www.youtube.com")
                    recognized_command = True
                elif "what is today" in processed_command:
                    speak("TODAY IS DIAPAWLI SIR ,HAPPY DIPAWLI !!")

                elif "go" in processed_command:
                    speak("as you command my lord sending wishes to all")
                    #send_whatsapp_messages_to_self()

                elif "open whatsapp" in processed_command:
                    open_whatsapp_in_chrome()
                    recognized_command = True
                elif "whatsapp message" in processed_command:
                    send_whatsapp_messages()
                    recognized_command = True
                elif "whatsapp message " in processed_command:
                    send_whatsapp_messages()
                    recognized_command = True
                elif "play music" in processed_command:
                    play_spotify_music()
                    recognized_command = True
                elif "search" in processed_command:
                    search_query = command.replace("search", "").strip()
                    search_on_web(search_query)
                    recognized_command = True
                elif"call k"    in processed_command:
                    handle_chat(mode="professional")
                    recognized_command=True
                elif "learn" in processed_command:
                    learn_command(command, custom_commands, language)
                    recognized_command = True
                elif "read news" in processed_command:
                    read_news()
                    recognized_command = True
                elif "add task" in processed_command:
                    add_task_by_voice(tasks)
                    recognized_command = True
                elif "remove task" in processed_command:
                    remove_task_by_voice(tasks)
                    recognized_command = True
                elif "speak task" in processed_command:
                    speak_tasks_by_voice(tasks)
                    recognized_command = True
                elif "shutdown" in processed_command:
                    speak("Shutting down. Goodbye!")
                    shutdown()
                    recognized_command = True
                elif "restart" in processed_command:
                    speak("Restarting. Be right back!")
                    restart()
                    recognized_command = True
                elif "sleep" in processed_command:
                    speak("Putting the system to sleep. Goodbye!")
                    system_sleep()
                    recognized_command = True
                elif "timer" in processed_command:
                    set_timer()
                    recognized_command = True
                elif "reminder" in processed_command:
                    set_reminder()
                    recognized_command = True
                elif "task" in processed_command:
                    speak_task_list(tasks)
                    recognized_command = True
                elif "open" in processed_command:
                    open_file(saved_paths)
                    recognized_command = True
                elif "new tab" in processed_command:
                    open_new_tab()
                    recognized_command = True
                elif "close tab" in processed_command:
                    close_current_tab()
                    recognized_command = True
                elif "tell me about" in processed_command:
                    #get_wikipedia_info()
                    diwali()
                    recognized_command = True
                elif "take note " in processed_command:
                    take_note()
                    recognized_command = True
                elif "take note" in processed_command:
                    take_note()
                    recognized_command = True
                elif "take a note " in processed_command:
                    take_note()
                    recognized_command = True
                elif "face" in processed_command:
                    #capture_images()
                    recognized_command = True
                elif "volume control" in processed_command:
                    volume_control()
                    recognized_command = True


                elif "play on youtube" in processed_command.lower():
                    video_query = command.lower().replace("play on youtube", "").strip()
                    play_youtube_video(video_query)
                    recognized_command = True
                elif "bad word" in processed_command:
                       badword()


                elif command in custom_commands:
                    speak({custom_commands[command]}, language)
                    subprocess.Popen(custom_commands[command], shell=True)
                    recognized_command = True

                else:
                    recognized_command = False
                    #best_match_score = 0
                    # Check for matches in the HTML responses
                    for item in html_responses:
                        if 'prompt' in item and 'response' in item:
                            # Convert prompt to lowercase for case-insensitive matching
                            prompt_text1 = preprocess_text(item['prompt'])
                            prompt_text = prompt_text1.lower()
                            # Check if the spoken command matches the lowercase prompt

                            """similarity_score = calculate_similarity(command.lower(), prompt_text)
                            if similarity_score > min_similarity_threshold and similarity_score > best_match_score:
                                best_match_score = similarity_score"""
                            if command.lower() in prompt_text:
                                 # If there is a match, print the corresponding response
                                speak("match found")
                                print("Match Found!")
                                print(f"Theory: {item['response']['theory']}")
                                print(f"Code: {item['response']['code']}")
                                recognized_command = True
                                break

                if not recognized_command:
                    print(f"Debug: Unrecognized command - {command}")
                    add_new_command_variation()


    #send_whatsapp_messages_to_self()
def play_youtube_video(query):
    driver = None
    port = None

    try:
        # Generate a random port in the range 9000-9999
        port = random.randint(9000, 9999)

        # Default Chrome path
        default_chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        # Attempt to open YouTube with the default path
        subprocess.Popen(
            [default_chrome_path, f'--remote-debugging-port={port}', '--new-window', 'https://www.youtube.com'])

        # Wait for Chrome to start (increase sleep duration if needed)
        time.sleep(5)

        # Set up WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = f"127.0.0.1:{port}"
        driver = webdriver.Chrome(options=chrome_options)

        # Wait for the YouTube page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("YouTube"))

        # Search for the video
        search_box = driver.find_element(By.NAME, 'search_query')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='contents']//ytd-video-renderer[1]")))

        # Click on the first video using the new XPath
        try:
            first_video = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//yt-formatted-string[@class='style-scope ytd-video-renderer'])[1]")))
            first_video.click()
        except TimeoutException:
            # Handle the case when the first element is not found
            print("The first video element is not found.")

        # Wait for the video to start playing
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ytp-inline-preview-ui']//div[1]")))
        time.sleep(5)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Close the browser window
        if driver:
            driver.quit()

    return driver, port

"""def take_note():
    speak("Please speak your note.")
    note_text = listen()

    if note_text:
        # Save the note to a file (you can customize the file path)
        note_filename = "notes.txt"
        with open(note_filename, "a") as note_file:
            note_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {note_text}\n")

        speak("Note saved successfully.")
    else:
        speak("Sorry, I couldn't understand the note.")"""


def volume_control():
    import cv2
    import mediapipe as mp
    import pyautogui

    x1 = y1 = x2 = y2 = 0

    webcam = cv2.VideoCapture(0)
    my_hands = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils

    while True:
        _, image = webcam.read()
        image = cv2.flip(image, 1)
        frame_height, frame_width, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output = my_hands.process(rgb_image)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(image, hand)
                landmarks = hand.landmark

                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)

                    if id == 8:
                        cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                        x1 = x
                        y1 = y

                    if id == 4:
                        cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                        x2 = x
                        y2 = y

            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4

            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)

            # Determine hand movement direction and scroll accordingly
            if y2 < y1:
                pyautogui.scroll(55)  # Scroll up
            elif y2 > y1:
                pyautogui.scroll(-55)  # Scroll down

            if dist > 20:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

        cv2.imshow("hand volume and scroll control using python", image)
        key = cv2.waitKey(10)

        if key == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()


def take_note():
    speak("Please speak your note. Say 'end note' to stop.")

    note_filename = "notes.txt"

    while True:
        note_text = listen()

        if note_text.lower() == "end note":
            speak("Stopping note-taking.")
            break

        if note_text:
            # Save the note to a file (you can customize the file path)
            with open(note_filename, "a") as note_file:
                note_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {note_text}\n")

            speak("Note saved successfully.")
        else:
            speak("Sorry, I couldn't understand the note.")
    return
def get_wikipedia_info():
    speak("Sure! What topic would you like to know more about?")
    topic = listen()

    if topic:
        wiki_wiki = wikipediaapi.Wikipedia('en', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        page_py = wiki_wiki.page(topic)

        if page_py.exists():
            # Extract and speak the summary
            summary = page_py.summary[:500]  # Limit the summary to avoid long responses
            speak(f"Here is a summary of {topic}: {summary}")
        else:
            speak(f"Sorry, I couldn't find information about {topic}. Please try another topic.")
    else:
        speak("Sorry, I couldn't understand the topic. Please try again.")

def shutdown():
    system_platform = platform.system().lower()
    if system_platform == 'windows':
        subprocess.Popen(["shutdown", "/s", "/t", "1"], shell=True)
    elif system_platform == 'linux':
        subprocess.Popen(["sudo", "shutdown", "-h", "now"])
    elif system_platform == 'darwin':
        subprocess.Popen(["sudo", "shutdown", "-h", "now"])
    else:
        print("Unsupported operating system for shutdown.")

def restart():
    system_platform = platform.system().lower()
    if system_platform == 'windows':
        subprocess.Popen(["shutdown", "/r", "/t", "1"], shell=True)
    elif system_platform == 'linux':
        subprocess.Popen(["sudo", "reboot"])
    elif system_platform == 'darwin':
        subprocess.Popen(["sudo", "reboot"])
    else:
        print("Unsupported operating system for restart.")

def sleep(seconds):
    time.sleep(seconds)

def system_sleep():
    system_platform = platform.system().lower()

    if system_platform == 'windows':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif system_platform == 'linux':
        os.system("systemctl suspend")
    elif system_platform == 'darwin':
        os.system("pmset sleepnow")
    else:
        print("Sleep not supported on this platform.")


def set_reminder():
    speak("Please speak the reminder message.")
    reminder_message = listen()

    if reminder_message:
        speak("Now, please speak the delay for the reminder.")

        # Check if the input contains a numeric value
        delay_minutes = extract_numeric_value(listen())

        if delay_minutes is not None and delay_minutes > 0:
            speak(f"Reminder set: {reminder_message}. I will remind you in {delay_minutes} minutes.")

            # Run the reminder in a separate thread
            reminder_thread = threading.Thread(target=run_reminder, args=(reminder_message, delay_minutes))
            reminder_thread.start()
        else:
            speak("Invalid input for delay. Please provide a positive integer.")
    else:
        speak("Sorry, I couldn't understand the reminder message.")


def run_reminder(reminder_message, delay_minutes):
    # Wait for the specified duration
    sleep(delay_minutes * 60)
    # Execute actions when the reminder is due
    speak(f"Reminder: {reminder_message}.")

# Function to set a timer with sound alert
def set_timer():
    speak("Please speak the duration for the timer.")
    duration_input = listen()
    duration_minutes = extract_numeric_value(duration_input)

    if duration_minutes is not None and duration_minutes > 0:
        speak(f"Timer set for {duration_minutes} minutes.")
        # Run the timer in a separate thread
        timer_thread = threading.Thread(target=run_timer, args=(duration_minutes,))
        timer_thread.start()
    else:
        speak("Invalid input for duration. Please provide a positive integer.")

def run_timer(duration_minutes):
    # Wait for the specified duration
    sleep(duration_minutes * 60)
    # Execute actions after the timer is complete
    speak("Time's up!")
    play_alert_sound()

def close_current_tab():
    try:
        # Use webbrowser to close the current tab
        webbrowser.hotkey('ctrl', 'w')
        return True
    except Exception as e:
        print(f"Error closing tab: {str(e)}")
        return False

def open_new_tab():
    try:
        # Use webbrowser to open a new tab
        webbrowser.open_new_tab('about:blank')
        return True
    except Exception as e:
        print(f"Error opening new tab: {str(e)}")
        return False


def open_file(saved_paths):
    speak("Please speak the name of the file you want to open.")
    file_name = listen()

    if file_name:
        # Check if the file_name is already in saved_paths
        if file_name.lower() in saved_paths:
            file_path = saved_paths[file_name.lower()]
        else:
            # If not found, prompt the user for the file path
            speak(f"Sorry, I couldn't find a saved path for {file_name}. Please provide the full path.")
            file_path = input("enter the path of the file:")

            # Save the new path for future reference
            if file_path:
                saved_paths[file_name.lower()] = file_path
                save_saved_paths(saved_paths)
            else:
                speak("No path provided. Cannot save for future reference.")

        # Check if the file_path exists
        if os.path.exists(file_path):
            try:
                # Open the file with the default application
                os.startfile(file_path)
                speak(f"Opening {file_name}.")
            except Exception as e:
                print(f"Error opening file: {str(e)}")
                speak("Sorry, there was an issue opening the file.")
        else:
            speak(f"Sorry, the file {file_name} does not exist at the specified path.")
    else:
        speak("Sorry, I couldn't understand the file name. Please try again.")

def save_saved_paths(saved_paths):
    with open("saved_paths.json", "w") as file:
        json.dump(saved_paths, file)

# Function to load the saved_paths dictionary
def load_saved_paths():
    try:
        with open("saved_paths.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def extract_numeric_value(input_text):
    try:
        # Attempt to extract numeric value from the input text
        numeric_value = int(next(filter(str.isdigit, input_text), None))

        # If the input contains "minute" or "minutes," multiply by 1 (default)
        if "minute" in input_text and numeric_value > 0:
            return numeric_value
        else:
            return None
    except ValueError:
        return None



# Function to play an alert sound
def play_alert_sound():
    try:
        alert_sound = pygame.mixer.Sound(r"D:\maruti\output.mp3")  # Replace with your sound file
        alert_sound.play()
    except pygame.error as e:
        print(f"Error playing sound: {str(e)}")


def play_spotify_music():
    # Add your Spotify API credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET",
                                                   redirect_uri="YOUR_REDIRECT_URI", scope="user-library-read"))

    # Add your favorite playlist URI or track URI
    playlist_uri = "spotify:playlist:YOUR_PLAYLIST_URI"

    sp.start_playback(context_uri=playlist_uri)



def search_on_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"searching {query}")




def learn_command(command, custom_commands, language='en'):
    speak("Sure! Do you want to manually input the command and action, or do you want to speak them?", language)
    choice = listen()

    if choice and "manual" in choice:
        manual_learn_command(command, custom_commands, language)
    elif choice and "speak" in choice:
        speak_learn_command(command, custom_commands, language)
    else:
        speak("Sorry, I couldn't understand your choice. Please try again.", language)

def manual_learn_command(command, custom_commands, language='en'):
    speak("Please manually input the command:", language)
    user_command = input("Enter the command: ")

    if user_command:
        speak("Please manually input the action associated with this command:", language)
        action = input("Enter the action: ")

        if action:
            custom_commands[user_command] = action
            speak(f"Command learned: {user_command} now associates with the action: {action}", language)
        else:
            speak("Sorry, the action cannot be empty. Please try again.", language)
    else:
        speak("Sorry, the command cannot be empty. Please try again.", language)

def speak_learn_command(command, custom_commands, language='en'):
    speak("Please speak the command:", language)
    user_command = listen()

    if user_command:
        speak("Please speak the action associated with this command:", language)
        action = listen()

        if action:
            custom_commands[user_command] = action
            speak(f"Command learned: {user_command} now associates with the action: {action}", language)
        else:
            speak("Sorry, I couldn't understand the action. Please try again.", language)
    else:
        speak("Sorry, I couldn't understand the command. Please try again.", language)

def translate_command(command, source_language, target_language='en'):
    translator = Translator(service_urls=['translate.googleapis.com'])
    translation = translator.translate(command, src=source_language, dest=target_language)
    return translation.text.lower()


def read_news():
    news_url = "https://example.com/news"  # Replace with the actual URL of the news page
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = [p.get_text() for p in soup.find_all('p')]
    news_text = ' '.join(paragraphs)

    speak(news_text, language='en')


def save_custom_commands(custom_commands):
    with open("custom_commands.json", "w") as file:
        json.dump(custom_commands, file)


import json

def load_custom_commands():
    try:
        with open("custom_commands.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Custom commands file not found. Creating an empty one.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON. Check if the file contains valid JSON syntax.")
        return {}
    except UnicodeDecodeError:
        print("Error decoding Unicode. Make sure the file is saved with UTF-8 encoding.")
        return {}

def open_whatsapp_in_chrome():
    driver = None
    try:
        # Generate a random port in the range 9000-9999
        port = random.randint(9000, 9999)

        # Default Chrome path
        default_chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        # Attempt to open WhatsApp with the default path
        subprocess.Popen([default_chrome_path, f'--remote-debugging-port={port}', 'https://web.whatsapp.com'])

        # Wait for Chrome to start (increase sleep duration if needed)
        time.sleep(10)

        # Set up WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = f"127.0.0.1:{port}"
        driver = webdriver.Chrome(options=chrome_options)

        # Wait for the WhatsApp page to load
        wait = WebDriverWait(driver, 30)
        wait.until(EC.title_contains("WhatsApp"))

        return driver, port
    except Exception as e:
        print(f"Error opening WhatsApp in Chrome with the default path: {str(e)}")

        # Ask the user for input if default path didn't work
        speak("The default path didn't work. Please enter the path to the Chrome executable.")
        chrome_path = input("User Input: ")

        try:
            # Attempt to open WhatsApp with the user-provided path
            subprocess.Popen([chrome_path, f'--remote-debugging-port={port}', 'https://web.whatsapp.com'])

            # Wait for Chrome to start (increase sleep duration if needed)
            time.sleep(10)

            # Set up WebDriver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.debugger_address = f"127.0.0.1:{port}"
            driver = webdriver.Chrome(options=chrome_options)

            # Wait for the WhatsApp page to load
            wait = WebDriverWait(driver, 30)
            wait.until(EC.title_contains("WhatsApp"))

            return driver, port
        except Exception as e:
            print(f"Error opening WhatsApp in Chrome with the user-provided path: {str(e)}")
            return None, None


def send_whatsapp_messages2(driver=None, port=None):
    if driver is None or port is None:
        driver, port = open_whatsapp_in_chrome()

        if driver is None:
            speak("Sorry, there was an issue opening WhatsApp. Please try again.")
            return

    while True:
        speak("Please say the contact name, and then the message.")
        user_input = listen()

        if user_input:
            # Split the input into contact name and message
            parts = user_input.split(" ", 1)
            if len(parts) == 2:
                contact_name = parts[0].strip()
                message = parts[1].strip()

                search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
                search_box.send_keys(contact_name)
                time.sleep(2)  # Wait for search results to load
                search_box.send_keys(Keys.RETURN)

                speak("Taking permission for sending. Do you want to proceed?")
                confirmation = listen()

                if confirmation and "fuck" in confirmation.lower():
                    try:
                        # Locate the message box and send the message
                        message_box = find_element_with_retry(driver, By.XPATH, "(//div[@contenteditable='true'])[2]")
                        if message_box:
                            message_box.click()
                            message_box.send_keys(message)
                            time.sleep(1.5)  # Adjust the timing as necessary
                            message_box.send_keys(Keys.ENTER)
                            speak("Message sent successfully.")
                        else:
                            speak("Message box not found. Sending cancelled.")
                    except Exception as e:
                        print(f"Error sending WhatsApp message: {str(e)}")
                        speak("Sorry, there was an issue sending the message.")
                else:
                    speak("Sending cancelled.")
            else:
                speak("Sorry, I couldn't understand the input. Please try again.")
        else:
            speak("Sorry, I couldn't understand the input. Please try again.")

        speak("Do you want to send another message?")
        another_message = listen()

        if another_message and "fuck" in another_message.lower():
            continue
        else:
            speak("Okay, if you need assistance with anything else, feel free to ask.")
            break
            pass
def send_whatsapp_messages(driver=None, port=None):
    if driver is None or port is None:
        driver, port = open_whatsapp_in_chrome()

        if driver is None:
            speak("Sorry, there was an issue opening WhatsApp. Please try again.")
            return

    while True:
        speak("Please say the contact name, and then the message.")
        user_input = listen()

        if user_input:
            # Split the input into contact name and message
            parts = user_input.split(" ", 1)
            if len(parts) == 2:
                contact_name = parts[0].strip()
                message = parts[1].strip()

                search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
                search_box.send_keys(contact_name)
                time.sleep(2)  # Wait for search results to load
                search_box.send_keys(Keys.RETURN)

                try:
                    # Locate the message box and send the message
                    message_box = find_element_with_retry(driver, By.XPATH, "(//div[@contenteditable='true'])[2]")
                    if message_box:
                        message_box.click()
                        message_box.send_keys(message)
                        time.sleep(1.5)  # Adjust the timing as necessary
                        message_box.send_keys(Keys.ENTER)
                        speak("Message sent successfully.")
                    else:
                        speak("Message box not found. Sending cancelled.")
                except Exception as e:
                    print(f"Error sending WhatsApp message: {str(e)}")
                    speak("Sorry, there was an issue sending the message.")
            else:
                speak("Sorry, I couldn't understand the input. Please try again.")
        else:
            speak("Sorry, I couldn't understand the input. Please try again.")

        speak("Do you want to send another message?")
        another_message = listen()

        if another_message and "ha" in another_message.lower():
            continue
        else:
            speak("Okay, if you need assistance with anything else, feel free to ask.")
            break
def play_alert_sound2():
    try:
        alert_sound = pygame.mixer.Sound(r"D:\maruti\WhatsApp Audio 2023-12-10 at 15.49.34_06aa5595.mp3")  # Replace with your sound file
        alert_sound.play()
    except pygame.error as e:
        print(f"Error playing sound: {str(e)}")

def badword():
    play_alert_sound2()


if __name__ == "__main__":
    morning_planning()
    speak("Hello! SIR WELCOME BACK, SO WHAT IS THE PLAN NOW")

    custom_commands = load_custom_commands()
    saved_paths = load_saved_paths()
    tasks = []
    while True:
        command = listen()
        if command:
            if "exit" in command:
                save_custom_commands(custom_commands)
                speak("jay! shree, krishna sir bye bye ")
                break
            command1 = command#preprocess_text(command)
            translated_command = command1 #translate_command(command, source_language='auto', target_language='en')
            run_command(translated_command, custom_commands)
            manage_tasks()
