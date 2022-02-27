import winreg
import sys
import os


while True:
    firstcontinuequestion = input("WARNING: This program modifies the registry. Please be careful using it. Continue? [y/n]")
    if (firstcontinuequestion == "n"):
        sys.exit("aborting...")
    elif (firstcontinuequestion == "y"):
        break
    else:
        print("Couldn't understand you. Please do it again.")
        continue


taskbar_bottom = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x000\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x80\x04\x00\x00\x80\x07\x00\x00\xb0\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'
taskbar_top = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x01\x00\x00\x000\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x80\x04\x00\x00\x80\x07\x00\x00\xb0\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'

def changeregistry(tob):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", 0, winreg.KEY_ALL_ACCESS) as sub_key:
            existing_binary_setting = winreg.EnumValue(sub_key, 0)[1]
            new_binary_setting = tob
            winreg.SetValueEx(sub_key, "SETTINGS", 0, winreg.REG_BINARY, new_binary_setting)

def restartexplorer():
    os.system("taskkill /f /im explorer.exe")
    os.system("start explorer")



while True:
    toporbottom = input("Do you want the taskbar to move to the top or to the bottom? [t/b]")
    if(toporbottom == "t"):
        changeregistry(taskbar_top)
        break
    elif(toporbottom == "b"):
        changeregistry(taskbar_bottom)
        break
    else:
        print("Couldn't understand you. Please do it again")
        continue

print("Registry changes successful")

while True:
    restartexplorerquestion = input("Would you like to restart explorer to see the changes? [y/n]")
    if (restartexplorerquestion == "n"):
        print("You will see the changes after the next explorer restart.")
        break
    elif(restartexplorerquestion == "y"):
        print("restarting explorer")
        restartexplorer()
        print("restart of explorer finished")
        break
    else:
        print("Couldn't understand you. Please try again")
        continue
