#from whatsapp import send_whatsapp_messages_to_self
import time
import datetime
import atexit
from speech_handler import listen
import json
from speak_function import speak
import pygame
pygame.mixer.init()
def load_tasks_from_file():
    filename = "tasks.txt"
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(": ", 1)
                if len(parts) == 2:
                    date_str, task_str = parts
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    descriptions = [desc.strip() for desc in task_str.split(',')]
                    tasks.append({"date": date, "descriptions": descriptions})

        return tasks
    except FileNotFoundError:
        return []
tasks = load_tasks_from_file()
print([tasks])
def speak_task_list(tasks):
    if not tasks:
        speak("Hey, you're all caught up! No pending tasks. Great job!")
        return

    for task in tasks:
        date_str = task['date'].strftime("%Y-%m-%d")
        speak(f"On {date_str}, you have the following tasks:")
        for i, description in enumerate(task['descriptions'], start=1):
            speak(f"Task {i}: {description}")


def add_task(tasks, new_task_description):
    today = datetime.date.today()

    # Check if there's already a set of tasks for today
    today_tasks = next((task for task in tasks if task['date'] == today), None)

    if today_tasks:
        today_tasks['descriptions'].append(new_task_description)
    else:
        tasks.append({"date": today, "descriptions": [new_task_description]})

    speak(f"New task added for today: '{new_task_description}'.")
    #speak_task_list(tasks)
    save_tasks_to_file(tasks)  # Save tasks to file after adding


def remove_task(tasks, task_index):
    today = datetime.date.today()

    # Find the index of the set of tasks for today
    today_index = next((i for i, task in enumerate(tasks) if task['date'] == today), None)

    if today_index is not None and 1 <= task_index <= len(tasks[today_index]['descriptions']):
        removed_description = tasks[today_index]['descriptions'].pop(task_index - 1)
        speak(f"Task {task_index} removed: '{removed_description}'. Great job!")
        #speak_task_list(tasks)
        save_tasks_to_file(tasks)  # Save tasks to file after removal
    else:
        speak("Invalid task index. Please provide a valid index.")

    # Update the task file with the modified tasks
    save_tasks_to_file(tasks)

def save_tasks_to_file(tasks):
    filename = "tasks.txt"

    with open(filename, "w") as file:  # Use 'w' to write/overwrite the file
        for task in tasks:
            date_str = task['date'].strftime("%Y-%m-%d")
            descriptions_str = ', '.join(task['descriptions'])
            file.write(f"{date_str}: {descriptions_str}\n")
    return




def morning_planning():
    # Check if tasks are already present for today's date
    tasks = load_tasks_from_file()
    today_tasks = [task for task in tasks if task['date'] == datetime.date.today()]

    if today_tasks:
        speak("Good morning! Your day has already been planned. Let me know if you need assistance.")
        return []

    current_time = datetime.datetime.now().time()

    # Check if the current time is between 7 AM and 12 PM (noon)
    if datetime.time(6, 0) <= current_time <= datetime.time(19, 0):
        speak("Good morning! uth ja bhai kitna soyega subah hogye, jai shree krishna or aaj ki planning karte hai. bta mujhe what are you going to do today?")

        new_tasks = []

        speak("You can start by telling me your first task.")

        while True:
            new_task = listen()

            # Check if the new_task is not None before trying to process it
            if new_task is not None:
                if "thank" in new_task.lower():
                #if new_task.lower() == "thank":
                    break

                add_task(new_tasks, new_task)
            else:
                speak("Sorry, I could not understand your audio. Please try again.")

        # Combine new tasks with existing tasks
        tasks += new_tasks

        speak("Great! Your tasks have been added. Remember, a well-planned day leads to success.")
        save_tasks_to_file(tasks)  # Save all tasks to file after planning
        txt_file_path = r"tasks.txt"

        # Call the function to send WhatsApp messages to yourself
        #send_whatsapp_messages_to_self(txt_file_path)

        return new_tasks
    else:
        speak("Good morning! It's not the planning time yet. Let me know if you need assistance later.")
        return []

# Assuming you have the load_tasks_from_file and save_tasks_to_file functions from previous code



def manage_tasks():
    tasks = load_tasks_from_file()
    atexit.register(save_tasks_to_file, tasks)

    help_asked = False  # Flag to keep track if help has already been asked

    while True:
        time.sleep(1800)

        # Check if there are tasks for today
        today_tasks = [task for task in tasks if task['date'] == datetime.date.today()]

        if not today_tasks:
            speak("Hey, you're all caught up! No pending tasks for today. Great job!")

        # Check if help has been asked
        if not help_asked:
            speak_task_list(today_tasks)
            speak("How are you doing with your tasks? Need any help?")
            response = listen().lower()

            if "completed" in response:
                speak("Which task would you like to mark as completed? Please provide the task number.")
                task_index_str = ''.join(c for c in response if c.isdigit())
                task_index = int(task_index_str)
                remove_task(tasks, task_index)
            elif "exit" in response:
                speak("Goodbye!")
                break
            else:
                speak("I'm here to help you. Let me know if you need anything.")
                help_asked = True  # Set the flag to True to avoid repeating the help message
        else:
            break  # Exit the loop if help has already been asked

# Assuming you have the necessary functions (load_tasks_from_file, save_tasks_to_file, speak_task_list, listen, add_task, remove_task) from your previous code


def speak_tasks_by_voice(tasks):
    print("Inside speak_tasks_by_voice function.")
    today = datetime.date.today()
    today_tasks = [task for task in tasks if task['date'] == today]

    if not today_tasks:
        speak("Hey, you're all caught up! No pending tasks for today. Great job!")
        return

    speak("Here are your tasks for today:")
    for i, task in enumerate(today_tasks, start=1):
        print("Inside the for loop for speaking the tasks")
        date_str = task['date'].strftime("%Y-%m-%d")
        speak(f"On {date_str}, you have the following tasks:")
        for j, description in enumerate(task['descriptions'], start=1):
            print("Inside j for loop.")
            speak(f"Task {j}: {description}")
    return

def add_task_by_voice(tasks):
    today = datetime.date.today()

    speak("What task would you like to add?")
    new_task = listen()

    # Check if there's already a set of tasks for today
    today_tasks = next((task for task in tasks if task['date'] == today), None)

    if today_tasks:
        today_tasks['descriptions'].append(new_task)
    else:
        tasks.append({"date": today, "descriptions": [new_task]})

    speak(f"New task added for today: '{new_task}'.")
    speak_task_list(tasks)
    save_tasks_to_file(tasks)  # Save tasks to file after adding
    return


def remove_task_by_voice(tasks):
    speak_task_list(tasks)
    speak("which task would you like to remove ")

    response = listen()

    if response:
        response = response.lower()

        if "yes" in response:
            add_task_by_voice(tasks)
        elif "no" in response:
            speak("Alright, let me know if you need anything else.")
        else:
            # Extract the numeric part from the response
            task_index_str = ''.join(c for c in response if c.isdigit())

            try:
                task_index = int(task_index_str)
                remove_task(tasks, task_index)
            except ValueError:
                speak("Invalid input. Please provide a valid task number.")
    else:
        speak("Could not understand audio. Please try again.")

    # Check if there are no tasks for the current day
    today_tasks = [task for task in tasks if task['date'] == datetime.date.today()]
    if not today_tasks:
        speak("Hey, you're all caught up! No pending tasks for today. Great job! Do you want to add a new task?")
        response = listen().lower()

        if "yes" in response:
            add_task_by_voice(tasks)
        else:
            speak("Alright, let me know if you need anything else.")
    return

