import pyautogui
import time

def remove(string):
    return string.replace("\t", "")

time.sleep(10)
name = r"D:\python\AutoTyper\code.txt"
with open(name) as f:
    data = f.read()
    data = remove(data)
    pyautogui.write(data,interval=0.05)
