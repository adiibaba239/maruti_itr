import csv
import os
import time
import logging
import subprocess
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import datetime


# Function to extract numerical digits from a string
def extract_numerical_digits(s):
    return ''.join(filter(str.isdigit, s))

csv_file_path = r"C:\Users\adity\Downloads\Contacts-03-Oct-10-23.csv"
def get_last_row_index(csv_file_path):
    with open(csv_file_path, mode='r',encoding='utf-8') as file:
        reader = csv.reader(file)
        total_rows = sum(1 for row in reader)
    return total_rows - 1
def send_whatsapp_messages_to_self(txt_file_path):
    def open_whatsapp_in_chrome():
        try:
            # Generate a random port in the range 9000-9999
            port = random.randint(9000, 9999)
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust the path as needed
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
            print(f"Error opening WhatsApp in Chrome: {str(e)}")
            return None, None

    # Initialize driver as None outside the try-except block
    driver = None

    try:
        # Open WhatsApp in Chrome with a random port
        driver, chosen_port = open_whatsapp_in_chrome()

        # Wait for QR code scan
        #input("Scan the QR code and press any key to continue")


        logging.basicConfig(filename='whatsapp_script.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Function to handle element click with retries
        def click_element_with_retry(element, max_retries=3):
            retries = 0
            while retries < max_retries:
                try:
                    element.click()
                    return True
                except ElementClickInterceptedException:
                    retries += 1
                    time.sleep(1.5)
            return False

        # Function to find an element with retries
        def find_element_with_retry(driver, by, value, max_retries=3):
            retries = 0
            while retries < max_retries:
                try:
                    element = driver.find_element(by, value)
                    return element
                except NoSuchElementException:
                    retries += 1
                    time.sleep(1.5)
            return None

        # Read the message from the .txt file
        r"""with open(txt_file_path, 'r') as file:
            today = datetime.datetime.now().strftime("%Y-%m-%d")  # Format: 'YYYY-MM-DD'
            message = ""
            current_date = None

            for line in file:
                line = line.strip()

                # Check if the line contains a date in 'YYYY-MM-DD' format
                if len(line) == 10 and line.count('-') == 2:  # Simple check for date format
                    current_date = line
                elif current_date == today and line:  # If current line is a task for today, add to message
                    message += line + "\n"

            message = message.strip()  # Remove any extra newline characters"""

        #def extract_and_format_today_tasks(txt_file_path):
        with open(txt_file_path, 'r') as file:
                today = datetime.datetime.now().strftime("%Y-%m-%d")  # Format today's date as 'YYYY-MM-DD'
                message = ""

                for line in file:
                    line = line.strip()

                    # Check if the line contains a task in the format 'YYYY-MM-DD: task description'
                    if ':' in line:
                        date_part, task_part = line.split(':', 1)  # Split line by the first colon

                        if date_part == today:  # If the date matches today's date
                            tasks = task_part.split(',')  # Split multiple tasks by comma
                            message = "Today's tasks are:\n"
                            for idx, task in enumerate(tasks, 1):
                                message += f"{idx}. {task.strip()}\n"  # Format as numbered list

                message = message.strip()  # Remove any extra newlines"""
                #return message
        r"""name = "Aditya"
        assistant_name = "Maruti AI"

        message = 
        """
        #start_row = int(input("Enter the starting row index (default is 1): ") or 1)
        start_row=1

        # Ask user for the last row index
        #end_row_input = input("Enter the last row index (press Enter for default): ")

        #end_row = int(end_row_input) if end_row_input else get_last_row_index(csv_file_path)
        end_row=get_last_row_index(csv_file_path)

        # Specify your own contact name
        print(f"The last row index is: {end_row}")

        logging.basicConfig(filename='whatsapp_script.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        your_name = "YOU"  # Change this to your WhatsApp name
        r"""with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            # Skip header if present

            for i, row in enumerate(reader, 1):
                if i < start_row:
                    continue

                if i > end_row:
                    break
                contact_name = row[1]  # Extract the contact name from each row
                raw_contact_number = row[2]  # Extract the raw contact number from each row

                # Extract only numerical digits from the raw contact number
                contact_number = extract_numerical_digits(raw_contact_number)
                if not contact_number or len(contact_number) < 10:
                    logging.warning(
                        f"Skipping contact {contact_name} because the contact number is empty or less than 10 digits.")
                    continue

                # Skip the contact if the number is empty or not a valid number
                if not contact_number:
                    logging.warning(f"Skipping contact {contact_name} because the contact number is empty.")
                    continue

                if not contact_number.startswith("+91"):
                    contact_number1 = "+91" + contact_number  # Add the +91 country code

                start_time = time.time()"""

                driver.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
                driver.find_element(By.XPATH, "//body").click()
                time.sleep(.2)
                driver.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)

                new_chat_button_xpath = "//div[@title='New chat']//span[1]"
                try:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, new_chat_button_xpath)))
                    new_chat_button = find_element_with_retry(driver, By.XPATH, new_chat_button_xpath)
                    if new_chat_button:
                        click_element_with_retry(new_chat_button)
                    else:
                        logging.error(f"Failed to open chat for {your_name}.")
                        return
                except Exception as e:
                    logging.error(f"Error opening chat for {your_name}: {str(e)}.")
                    return

                time.sleep(1)  # Adjust the timing as necessary

                # Input your name in the chat search box
                chat_box = find_element_with_retry(driver, By.XPATH, "(//div[@contenteditable='true'])[1]")
                if chat_box:
                    chat_box.click()
                    chat_box.send_keys(your_name)
                    time.sleep(.5)  # Adjust the timing as necessary
                    chat_box.click()
                    time.sleep(.5)
                    chat_box.send_keys(Keys.ENTER)
                else:
                    driver.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
                    logging.error(f"Chat box not found for {your_name}.")
                    return

                time.sleep(1.3)  # Adjust the timing as necessary

                # Input the message in the chat text box
                try:
                    message_box = find_element_with_retry(driver, By.XPATH, "(//div[@contenteditable='true'])[2]")
                    if message_box:
                        print("entered in message box")
                        message_box.click()
                        print("message box clicked")
                        time.sleep(.2)
                        message_box.send_keys(message)

                        print("entered in message box2")
                        print(message)
                        time.sleep(1.5)  # Adjust the timing as necessary
                        message_box.send_keys(Keys.ENTER)
                        driver.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
                    else:
                        driver.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
                        logging.error(f"Message box not found for {your_name}.")
                except Exception as e:
                    logging.error(f"Error sending message to {your_name}: {str(e)}.")
                time.sleep(1)
                driver.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)

        # Open a new chat


    finally:
        if driver:
            driver.quit()


# Path to the .txt file containing the message
