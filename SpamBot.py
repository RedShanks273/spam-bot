import pyautogui
import time
time.sleep(5)               #if you need more time to get on the Tab, just set the time up
f = open("spam", 'r')       #if your message isn´t named "spam", then just change it in that how you named the document
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")