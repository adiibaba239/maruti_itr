import pyautogui
import time


def send_whatsapp_messages(message, count):
    # Adding a short delay to give you time to place the cursor in the message box
    print("Place your cursor in the WhatsApp message box within the next 5 seconds.")
    time.sleep(5)

    for _ in range(count):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(0.4)  # Short delay to ensure messages are sent smoothly


# Example usage
send_whatsapp_messages("Happy Birthday,Mittali 🎉"
, 40)  # Customize message and count
