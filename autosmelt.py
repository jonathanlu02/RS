#####autosmelt#####

'''
Simple auto click macro that clicks on a furnace and smelts item.
NOTE: do not move screen after starting program.
'''

import pyautogui
import time
import random


duration_m = input("How long do you want to run this program for (minutes)? ")

print("\nProgram will start in: ")
for x in range(3,0,-1):
    print(x)
    time.sleep(1)
    
x1 = 100
y1 = 40

mid_x1 = 950
mid_y1 = 700

print("\nChecking the four corners of furnace to confirm valid location...")

#furnace
pyautogui.moveTo(mid_x1-x1, mid_y1-y1, 0.5)
pyautogui.click()

pyautogui.moveTo(mid_x1+x1, mid_y1-y1, 0.5)
pyautogui.click()

pyautogui.moveTo(mid_x1+x1, mid_y1+y1, 0.5)
pyautogui.click()

pyautogui.moveTo(mid_x1-x1, mid_y1+y1, 0.5)
pyautogui.click()
time.sleep(1)

duration_s = float(duration_m)*60

t_current = 0
t_start = time.time()  # because time.time() is current time, not 0

random_cis = random.randint(98,102)
t_cis = 0

drag_time1 = float(random.randint(200,300))/1000

t_tick = float(random.randint(1000,1200))/1000

while t_current < t_start + duration_s:
    time.sleep(0.1)  # drastically decrease cpu usage, sleep for 100ms

    if t_current >= t_start + t_cis + random_cis:
        random_cis = random.randint(88,94)
        t_cis += random_cis
        
        # move cursor to forge (location 1)
        x1_offset = random.randint(-x1,x1)
        y1_offset = random.randint(-y1,y1)
        pyautogui.moveTo(mid_x1 + x1_offset, mid_y1 + y1_offset, drag_time1)
        pyautogui.click()  #click the forge

        time.sleep(t_tick)  # wait for tick to process action

        # press space to confirm smelting the ores
        # space seems bugged, sometimes does not press, have multiple to ensure
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')

        time.sleep(t_tick)

        # use prayer regen on slot 9
        pyautogui.keyDown('9')
        pyautogui.keyUp('9')
        
    t_current = time.time()
