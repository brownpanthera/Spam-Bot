import pyautogui
from time import sleep
sleep(5)
f = open("text.txt", 'r')
for word in f:
 pyautogui.typewrite(word)
 pyautogui.press("enter")