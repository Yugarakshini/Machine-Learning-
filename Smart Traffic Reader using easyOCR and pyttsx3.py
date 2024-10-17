#!/usr/bin/env python
# coding: utf-8

# In[1]:


import easyocr
import cv2
from matplotlib import pyplot as plt
import pyttsx3  # Text-to-speech library
import time  # For adding pauses


# In[2]:


# Text-to-speech engine initialization
engine = pyttsx3.init()


# In[3]:


# Set the speech rate for clarity
engine.setProperty('rate', 140)


# In[4]:


# Set Indian English voice (replace with the correct voice ID)
voices = engine.getProperty('voices')
for voice in voices:
    if 'en_IN' in voice.languages:  # Check for Indian English accent
        engine.setProperty('voice', voice.id)
        break


# In[5]:


def speak_text(text):
    time.sleep(0.2)  # Small pause before speaking
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Ensure speech is complete
    time.sleep(0.3)  # Pause after speaking for clarity


# In[9]:


# Function to let the user choose an image and perform OCR + speech conversion
def image_to_speech():
    # List of image file paths
    image_paths = [
        'sign.png',  # Image 1
        'caution1.jpg',  # Image 2
        'caution2.png',  # Image 3
        'caution3.png',  # Image 4
        'caution4.jpg',# Image 5
    ]
    
    # Prompt the user to select an image number (1 to 5)
    img_num = int(input("Enter the image number (1-5): ")) - 1
    
    # Ensure the user input is within the valid range
    if img_num < 0 or img_num >= len(image_paths):
        error_message = "Invalid input. Please select a number between 1 and 5."
        print(error_message)
        speak_text(error_message)  # Voice output for the invalid input message
        return

    # Load the selected image
    IMAGE_PATH = image_paths[img_num]
    
    # Perform OCR on the selected image
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH)

    # Drawing bounding boxes around detected text and converting to speech
    img = cv2.imread(IMAGE_PATH)
    spacer = 100
    font = cv2.FONT_HERSHEY_SIMPLEX

    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]

        # Draw rectangle and add text to the image
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15
        
        # Speak the detected text
        speak_text(text)

    # Display the image with bounding boxes and text
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


# In[11]:


# Call the function
image_to_speech()


# In[ ]:




