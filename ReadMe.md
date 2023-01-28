## Apex "HUD is Up" Alert.

##### Notifies the user that the Apex HUD is up. This is for users who are attempting Apex challenges without a hud. This can be modified further to automatically hide the hud. This is a "safer" version. 

### Requirements
1) Python3+ Installed
2) PyAutoGui/Pillow/OpenCV PIP packages installed
3) Standard Windows Deployment (7/8/10/11)
4) 1080 monitor

### Install
1) Download the ZIP
2) Extract the ZIP to Downloads, leaving the name of the folder the same
3) Open the folder, and shift-right click in any void space. Select the "Open PowerShell window here" option.
4) ![image](https://user-images.githubusercontent.com/91140740/215049885-476ac2e3-1adc-4af9-836a-02babc6adeb0.png)
5) Run the command "python .\HudAlert.py"
6) You will now hear a chime anytime your HUD comes up


### Quick Overview
This script utilizes a small JPG of the "squads left" section of the screen along with pyautogui, to determine if the "HUD" is up. Given the amount of moving items in this game, this felt like one of the only "solid" pieces that is consistent when HUD is up. Views like Grenades, Ammo, Weapons, Teammates are all in flux, where as the text will always remain. Once the HUD is detected, the script will play a chime found natively in Windows. 
