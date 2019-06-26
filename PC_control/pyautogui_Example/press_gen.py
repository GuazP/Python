from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import time

i = 0
for x in range(int(60*3)):
    time.sleep(60)
    typewrite(str(i))
    press("backspace")

time.sleep(60*9)

press("enter")
time.sleep(3.24)
keyDown("ctrl")
press("q")
keyUp("ctrl")

