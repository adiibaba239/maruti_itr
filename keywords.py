import json
import pyttsx3
from speech_handler import speak, listen
import speech_recognition as sr

def load_keywords():
    try:
        with open('commands.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_keywords(keywords):
    with open('commands.json', 'w', encoding='utf-8') as file:
        json.dump(keywords, file, indent=2)

def display_keywords(keywords):
    print("Select a keyword:")
    for i, keyword in enumerate(keywords, start=1):
        print(f"{i}. {keyword}")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number corresponding to the keyword: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_command(selected_keyword):
    return input(f"Please speak a new command for '{selected_keyword}': ") or listen()


def listen_for_command():
    # Simulate listening for a command
    return input("Please speak your command: ")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def add_command_variation():
    # Read the existing keywords from the JSON file
    keyword_variations = load_keywords()

    # Extract all keywords from the JSON object
    all_keywords = list(keyword_variations.keys())

    # Speak the prompt before displaying the list of keywords
    speak("Sorry, I am in a learning stage. If the command you just spoke associates with any of these keywords, "
          "please choose the number and say the command, and I will learn that.")

    # Display the list of keywords to the user
    display_keywords(all_keywords)

    try:
        # Allow the user to choose a keyword
        selected_index = listen() or get_user_choice() - 1
        selected_keyword = all_keywords[selected_index]
        print(f"You selected: {selected_keyword}")

        # Listen for the new command or take input
        new_command_variation = listen() or input("enter the new command:")  # You can replace this line with get_user_command(selected_keyword) if needed

        # Update the data structure with the new variation
        if selected_keyword in keyword_variations:
            keyword_variations[selected_keyword].append(new_command_variation)
        else:
            keyword_variations[selected_keyword] = [new_command_variation]

        # Write the updated data structure back to the JSON file
        save_keywords(keyword_variations)

        print(f"New command variation added for '{selected_keyword}': {new_command_variation}")
    except IndexError:
        print("Invalid choice. Please select a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# If you want to make the code importable, you can define a function that encapsulates the functionality
def add_new_command_variation():
    add_command_variation()

# Call the function to add a new command variation
if __name__ == "__main__":
    add_new_command_variation()
