import pytesseract
from PIL import Image
import mss

# Set up pytesseract (ensure Tesseract is installed and configured)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Modify path as necessary


def capture_and_analyze_screen():
    # Capture screenshot
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])  # Grab the primary monitor
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

    # OCR on captured image
    text = pytesseract.image_to_string(img)

    return text


# Test function
screen_text = capture_and_analyze_screen()
print("Screen content:", screen_text)
