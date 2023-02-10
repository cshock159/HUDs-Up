## Apex "HUD is Up" Alert v1.0.3.

##### Detects and notifies/auto-closes the Apex Legends Heads Up Display (HUD). 

### Updates
1.0.3 includes an update with auto saving of configurations used previously. To enable the auto save, simply choose your options, start Huds-Up, and when you're done, exist the program. Values will be automatically saved.

### Requirements
1) Standard Windows Deployment (7/8/10/11)
2) Apex Button Hints enabled.

### Install
1) Download the ZIP
2) Extract to wherever you want
3) Open the HUDAlert folder and run HudAlert.exe

### Options
![image](https://user-images.githubusercontent.com/91140740/216475449-9893ef0c-d505-47a1-9e03-be4053aa9631.png)
1) Start/Stop : Super self explanatory. When clicking "Start", HUDs-Up will start with the options selected below.
2) Browse : Allows you to select your own custom image. This is important if you are using a monitor that is NOT 1080.
### IF YOU CHANGE ANY OF THESE OPTIONS AFTER THE PROGRAM IS STARTED, YOU MUST CLICK "UPDATE OPTIONS"
3) Confidence : This allows you to adjust how "sensitive" the program is. The higher your confidence, the less sensitive the program will be. You may start having issues if your confidence is set lower than .5.
4) Frequency : Allows you to determine how often the HUDs-Up checks for the HUD. This is purely personal preference
5) Audio Chime : If this is selected, an Audio Chime will be played with HUDs-Up detects the HUD. Unchecking this removes the chime. 
6) Auto Close HUD : This will auto close the HUD by pressing the key combo 7+esc. If you do not use this default combo, this will not work for you.
7) Update Options : You must click this to restart the program if you change any options AFTER the program is already running.

### Quick Overview
This script utilizes a small JPG of the "M" map section of the screen along with pyautogui, to determine if the "HUD" is up. Given the amount of moving items in this game, this felt like one of the only "solid" pieces that is consistent when HUD is up. Views like Grenades, Ammo, Weapons, Teammates are all in flux, where as the M will always remain. Once the HUD is detected, the script will play an alert and auto close the HUD by default. 

HUDs-Up was designed to work with as many different Apex modes as possible. It currently works in Pubs, Ranked and Arenas. LTMs have not been tested.
