import time
import pyautogui as auto
from time import sleep

# Starting
print("Starting in 5 seconds")
time.sleep(1)
print("Starting in 4 seconds")
time.sleep(1)
print("Starting in 3 seconds")
time.sleep(1)
print("Starting in 2 seconds")
time.sleep(1)
print("Starting in 1 seconds")
time.sleep(1)
print("Let's go!")
time.sleep(1)

# Work in progress
s = 0
while True:
    auto.write(':3')
    s += 1
    auto.press('enter')
    print(s)
