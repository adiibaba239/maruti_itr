import speech_recognition as sr
import pyautogui
import cv2
import numpy as np
import time

# Function to listen for voice commands
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        command = None
        print("Could not understand the command.")
    return command

# Function to find and click the close button based on template matching
def click_close_button():
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)  # Convert to numpy array
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # Convert color for OpenCV

    # Load the close button template
    close_button_template = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, close_button_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Adjust threshold as needed
    locations = np.where(result >= threshold)

    # If any matches found, click on the first match
    if len(locations[0]) > 0:
        x, y = locations[1][0], locations[0][0]
        # Adjust click point to center of the detected area
        h, w = close_button_template.shape
        pyautogui.click(x + w // 2, y + h // 2)
        print("Close button clicked.")
    else:
        print("Close button not found.")

# Main function to listen and respond to commands
def main():
    print("Maruti Assistant Active. Awaiting voice command...")

    while True:
        command = listen_command()

        if command:
            if "close chrome" in command or "close browser" in command:
                click_close_button()
            elif "exit" in command or "stop" in command:
                print("Exiting Maruti Assistant.")
                break
        time.sleep(2)

if __name__ == "__main__":
    main()
