import winreg, os, tkinter, threading, subprocess


# Restarts the explorer in an independent process
def restart_explorer():
    os.system("taskkill /f /im explorer.exe")
    subprocess.Popen(['explorer.exe'], close_fds=True, creationflags=0x00000008)

# Changes the location of the taskbar
def change_taskbar(TopBottom):
    # Value init
    taskbar_bottom = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x000\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x80\x04\x00\x00\x80\x07\x00\x00\xb0\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'
    taskbar_top = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x01\x00\x00\x000\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x80\x04\x00\x00\x80\x07\x00\x00\xb0\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", 0, winreg.KEY_ALL_ACCESS) as sub_key:
            existing_binary_setting = winreg.EnumValue(sub_key, 0)[1]
            if TopBottom == "Top":
                new_reg_set = taskbar_top
            else:
                new_reg_set = taskbar_bottom
            winreg.SetValueEx(sub_key, "SETTINGS", 0, winreg.REG_BINARY, new_reg_set)

# Thread init
class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    # UI calculation
    def run(self):
        # Base window
        root = tkinter.Tk()
        root.title("Windows 11 Taskbar location changer")

        # Warning label
        warn_label = tkinter.Label(root, text="WARNING: This tool modifies the registry! Be careful while using it.")
        warn_label.pack()

        # Top or Bottom buttons
        top_button = tkinter.Button(root, text="Change to Top", command= lambda: change_taskbar("Top"))
        bottom_button = tkinter.Button(root, text="Change to Bottom", command=lambda: change_taskbar("Bottom"))
        top_button.pack()
        bottom_button.pack()

        # Restart Explorer label and button
        restart_label = tkinter.Label(root, text="The changes will get visible after restarting Explorer. Do you want to do that now? ")
        restart_button = tkinter.Button(root, text="Restart Explorer", command=lambda: restart_explorer())
        restart_label.pack()
        restart_button.pack()

        # Window run
        root.mainloop()

if __name__ == '__main__':
    GUI_thread = GUI()
    GUI_thread.run()


