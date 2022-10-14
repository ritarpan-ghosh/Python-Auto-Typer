from winreg import HKEY_LOCAL_MACHINE
import pyautogui
import time

msg = input("Enter the massage: ")
times = int(input("Enter how many times you want to repeate: "))
new_line = input("Do you want a new line of enter after every line ? (y/n): ")
print("You have only 10 seconds to put the cursor in the right place.")

num = 0
time.sleep(10)
while(num<times):
    pyautogui.PAUSE = 0.01
    pyautogui.write(msg, interval=0.15)
    if new_line == 'y': 
        pyautogui.press('enter')
    num = num + 1