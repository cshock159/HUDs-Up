set /p ver="Enter the version number of this build to continue: "
set ver=%ver: =%
pyinstaller --noconfirm --log-level=WARN ^
    --onefile --noconsole ^
    --icon=.\icons\forbidden.ico ^
    --uac-admin ^
    HudAlert.py 

copy .\resources\* .\dist\
rename .\dist "Huds-Up-v%ver%"
cd "C:\Program Files\7-Zip\"
"C:\Program Files\7-Zip\7z.exe" a "C:\users\cshoc\Desktop\HUDs-Up-Releases\Huds-Up-V%ver%.zip" "C:\users\cshoc\downloads\HudAlert\Huds-Up-V%ver%"