r"""import pytesseract
from PIL import Image
import mss

# Set up pytesseract (ensure Tesseract is installed and configured)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Modify path as necessary


def capture_and_analyze_chat_area():
    # Define the region for the chat area (modify these coordinates based on your screen resolution and desired area)
    chat_area = {
        "left": 270,  # X coordinate of the top-left corner
        "top": 100,  # Y coordinate of the top-left corner
        "width": 2000,  # Width of the chat area
        "height": 600  # Height of the chat area
    }

    # Capture screenshot of the specified area
    with mss.mss() as sct:
        screenshot = sct.grab(chat_area)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

    # OCR on the captured image
    text = pytesseract.image_to_string(img)

    return text


# Test the function
screen_text = capture_and_analyze_chat_area()
print("Chat area content:", screen_text)
"""
import pytesseract
from PIL import Image
import mss
import time

# Set up pytesseract (ensure Tesseract is installed and configured)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Modify path as necessary

def capture_chat_area(chat_area):
    # Capture screenshot of the specified area
    with mss.mss() as sct:
        screenshot = sct.grab(chat_area)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
    return img

def get_text_from_image(img):
    # Use OCR on the captured image
    text = pytesseract.image_to_string(img)
    return text.strip()

def monitor_chat_area():
    # Define the region for the chat area (modify these coordinates as needed)
    chat_area = {
        "left": 270,
        "top": 100,
        "width": 2000,
        "height": 600
    }

    last_text = ""  # Variable to store the previous text in the chat area

    while True:
        # Capture the chat area and extract text
        img = capture_chat_area(chat_area)
        current_text = get_text_from_image(img)

        # Check if the text has changed
        if current_text != last_text:
            #print("New message detected!")
            #print("Chat area content:", current_text)
            last_text = current_text
            return current_text
              # Update the last_text to current

        # Wait for a specified interval before checking again
        time.sleep(2)  # Check every 2 seconds (adjust as needed)

# Start monitoring the chat area
monitor_chat_area()
