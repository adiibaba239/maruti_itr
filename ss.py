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


# Function to extract numerical digits from a string
def extract_numerical_digits(s):
    return ''.join(filter(str.isdigit, s))


# Function to get the last row index of a CSV file
def get_last_row_index(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        total_rows = sum(1 for row in reader)
    return total_rows - 1


# Function to open WhatsApp in Chrome
def open_whatsapp_in_chrome():
    try:
        port = random.randint(9000, 9999)
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust the path as needed
        subprocess.Popen([chrome_path, f'--remote-debugging-port={port}', 'https://web.whatsapp.com'])

        time.sleep(10)  # Wait for Chrome to start

        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = f"127.0.0.1:{port}"
        driver = webdriver.Chrome(options=chrome_options)

        wait = WebDriverWait(driver, 30)
        wait.until(EC.title_contains("WhatsApp"))

        return driver
    except Exception as e:
        print(f"Error opening WhatsApp in Chrome: {str(e)}")
        return None


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


# Function to extract contacts from CSV
def extract_contacts_from_csv(csv_file_path, start_row=1, end_row=None):
    contacts = []  # Initialize a list to store contact tuples (name, number)

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present

        for i, row in enumerate(reader, 1):
            if i < start_row:
                continue
            if end_row is not None and i > end_row:
                break

            contact_name = row[1].strip()  # Extract the contact name
            raw_contact_number = row[2].strip()  # Extract the contact number
            contact_number = extract_numerical_digits(raw_contact_number)

            # Skip invalid contacts
            if len(contact_number) < 10:
                logging.warning(f"Skipping contact {contact_name} because the contact number is invalid.")
                continue

            contacts.append((contact_name, contact_number))
    return contacts


# Function to send WhatsApp messages
def send_whatsapp_messages_to_self():
    driver = open_whatsapp_in_chrome()
    if driver is None:
        return

    logging.basicConfig(filename='whatsapp_script.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Custom message to send
    name = "Aditya"
    assistant_name = "Maruti AI"
    message = f"""Happy Diwali from {name} sent by {assistant_name}!

    May this festival of lights brighten your life with happiness, prosperity, and endless joy. 
    May the lamps of Diwali illuminate your heart and fill your days with success and peace. 
    Wishing you and your loved ones a safe, sparkling, and joyous Diwali filled with love, laughter, and light!

    Warmest wishes,
    Aditya
    """

    csv_file_path = r"C:\Users\adity\Downloads\Contacts-03-Oct-10-23.csv"
    contacts = extract_contacts_from_csv(csv_file_path)

    try:
        for contact_name, contact_number in contacts:
            print(f"Processing contact: {contact_name} with number: {contact_number}")

            # Open chat for the contact
            new_chat_button_xpath = "//div[@title='New chat']//span[1]"
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, new_chat_button_xpath)))
                new_chat_button = find_element_with_retry(driver, By.XPATH, new_chat_button_xpath)
                if new_chat_button:
                    click_element_with_retry(new_chat_button)
                else:
                    logging.error(f"Failed to open chat for {contact_number}.")
                    continue
            except Exception as e:
                logging.error(f"Error opening chat for {contact_number}: {str(e)}.")
                continue

            time.sleep(1)  # Adjust the timing as necessary

            # Input the contact number in the chat search box
            chat_box = find_element_with_retry(driver, By.XPATH, "(//div[@contenteditable='true'])[1]")
            if chat_box:
                chat_box.click()
                chat_box.send_keys(contact_number)
                time.sleep(0.5)  # Adjust the timing as necessary
                chat_box.send_keys(Keys.ENTER)
            else:
                logging.error(f"Chat box not found for {contact_number}.")
                continue

            time.sleep(1.3)  # Adjust the timing as necessary

            # Input the message in the chat text box
            message_box = find_element_with_retry(driver, By.XPATH, "(//div[@contenteditable='true'])[2]")
            if message_box:
                message_box.click()
                time.sleep(0.2)
                message_box.send_keys(message)
                time.sleep(1.5)  # Adjust the timing as necessary
                message_box.send_keys(Keys.ENTER)
                print(f"Message sent to {contact_name} ({contact_number}).")
                logging.info(f"Message sent to {contact_name} ({contact_number}).")
            else:
                logging.error(f"Message box not found for {contact_number}.")

            time.sleep(2)  # Delay before processing the next contact

    finally:
        if driver:
            driver.quit()


# Call the main function to send messages
send_whatsapp_messages_to_self()
