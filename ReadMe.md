## Apex "HUD is Up" Alert.

##### Detects and notifies/auto-closes the Apex Legends Heads Up Display (HUD).

### Requirements
1) Python3+ Installed
2) PyAutoGui/Pillow/OpenCV/threading/PySimpleGUI/pydirectinput/winsound
3) Standard Windows Deployment (7/8/10/11)
4) 1080 monitor
5) Apex Menu ToolTips enabled.

### Install
1) Download the ZIP
2) Extract the ZIP to Downloads, leaving the name of the folder the same
3) Open the folder, and shift-right click in any void space. Select the "Open PowerShell window here" option.
  NOTE: You MUST run the program with the same permission level as Apex Legends. If you run Origin/Apex as admin, you must run this as admin.
4) ![image](https://user-images.githubusercontent.com/91140740/215049885-476ac2e3-1adc-4af9-836a-02babc6adeb0.png)
5) Run the command "python .\HudAlert.py"


### Quick Overview
This script utilizes a small JPG of the "M" map section of the screen along with pyautogui, to determine if the "HUD" is up. Given the amount of moving items in this game, this felt like one of the only "solid" pieces that is consistent when HUD is up. Views like Grenades, Ammo, Weapons, Teammates are all in flux, where as the M will always remain. Once the HUD is detected, the script will play an alert and auto close the HUD by default. 
