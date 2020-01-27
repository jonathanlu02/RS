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
    
x1 = 15
y1 = 15

mid_x1 = 957
mid_y1 = 652

print("\nChecking the four corners of dwarf trader to confirm valid location...")

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

random_cis = random.randint(3,8)
random_cis1 = random.randint(290,305)
random_cis2 = random.randint(560,640)
random_cis3 = random.randint(320,340)
t_cis = 0
t_cis1 = 0
t_cis2 = 0
t_cis3 = 0

drag_time1 = float(random.randint(200,300))/1000

t_tick = float(random.randint(1000,1200))/1000

while t_current < t_start + duration_s:
    time.sleep(0.1)  # drastically decrease cpu usage, sleep for 100ms

    if t_current >= t_start + t_cis + random_cis: #clicking randomly
        random_cis = random.randint(2,4)
        t_cis += random_cis
        
        # move cursor to forge (location 1)
        x1_offset = random.randint(-x1,x1)
        y1_offset = random.randint(-y1,y1)
        pyautogui.moveTo(mid_x1 + x1_offset, mid_y1 + y1_offset, drag_time1)
        pyautogui.click()  #click the trader

    if t_current >= t_start + t_cis1 + 300: #crystal mask
        random_cis1 = random.randint(290,305)
        t_cis1 += random_cis1
        pyautogui.keyDown('7')
        pyautogui.keyUp('7')

    if t_current >= t_start + t_cis2 + 600: #prayer renewal
        random_cis2 = random.randint(560,640)
        t_cis2 += random_cis2
        pyautogui.keyDown('8')
        pyautogui.keyUp('8')
        
    if t_current >= t_start + t_cis3 + 330: #ancient elven ritual shard
        random_cis3 = random.randint(320,340)
        t_cis3 += random_cis3
        pyautogui.keyDown('9')
        pyautogui.keyUp('9')
    
    t_current = time.time()
