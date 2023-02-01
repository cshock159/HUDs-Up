import pyautogui
import pydirectinput
import time
import winsound
import os

user = os.getlogin()

# The path to the image file that we want to search for on the screen
image_file = 'C:/users/' + user + '/Downloads/HUDAlert/HudsUp.jpg'

# If the image was found on the screen
while(1==1):
    image_location = pyautogui.locateOnScreen(image_file,confidence=.9)
    if image_location is not None:
        winsound.PlaySound('C:/Windows/Media/Windows Battery Critical.wav', winsound.SND_FILENAME)
        pydirectinput.keyDown('7')
        pydirectinput.keyDown('esc')
        pydirectinput.keyUp('esc')
        pydirectinput.keyUp('7')
    time.sleep(5)