import pyautogui
import time
import random
import winsound

# The path to the image file that we want to search for on the screen
image_file = 'C:/users/cshoc/Downloads/HudsUp.jpg'

# If the image was found on the screen
while(1==1):
    image_location = pyautogui.locateOnScreen(image_file, confidence=.75)
    if image_location is not None:
        # Get the coordinates of the image
        winsound.PlaySound('C:/Windows/Media/Windows Battery Critical.wav', winsound.SND_FILENAME)
    time.sleep(5)