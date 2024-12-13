

import cv2
import os
import numpy as np
import face_recognition as fr

# Function to capture and save images from different angles
def capture_images(camera, person_name, image_count=100):
    print(f"Capturing images for {person_name}. Look at the camera and turn your face during the process!")

    images = []
    labels = []

    for i in range(image_count):
        ret, frame = camera.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find the face location in the image
        face_locations = fr.face_locations(rgb_frame)

        if len(face_locations) > 0:
            # Take the first face location (you might want to handle multiple faces differently)
            face_location = face_locations[0]

            # Extract the region of interest (ROI)
            face_roi = rgb_frame[face_location[0]:face_location[2], face_location[3]:face_location[1]]

            # Resize the face image to a consistent size (e.g., 100x100 pixels)
            resized_face = cv2.resize(face_roi, (100, 100))

            images.append(resized_face)
            labels.append(person_name)

            # Draw rectangle around the face
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (0, 255, 0), 2)

        cv2.imshow('Capture Images', frame)
        cv2.waitKey(500)

    return images, labels

# Path to the directory to save captured images
capture_dir = r"D:\pythonProjectd\pythonProject\maruti2.0\facemodel"

# Create the capture directory if it doesn't exist
os.makedirs(capture_dir, exist_ok=True)

# Open a connection to the camera (you may need to adjust the camera index)
camera = cv2.VideoCapture(0)

# Prompt user to enter their name
person_name = input("Enter your name: ")

# Capture and save images from different angles
captured_images, labels = capture_images(camera, person_name)

# Release the camera
camera.release()
cv2.destroyAllWindows()

# Convert the data to NumPy arrays
captured_images = np.asarray(captured_images)
labels = np.asarray(labels)

# Create an empty list to store the face encodings
face_encodings = []

# Loop through each captured image
for image in captured_images:
    # Generate the face encoding for the ROI
    face_encoding = fr.face_encodings(image)

    if len(face_encoding) > 0:
        # Take the first face encoding (you might want to handle multiple faces differently)
        face_encoding = face_encoding[0]

        # Append the face encoding to the list
        face_encodings.append(face_encoding)

# Save the face encodings and labels to a file
np.savez(os.path.join(capture_dir, f"{person_name}_encodings.npz"), face_encodings=face_encodings, labels=labels)

print(f"Training for {person_name} completed, and encodings saved to {person_name}_encodings.npz.")
