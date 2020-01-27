#####auto-clicker macro v1.0#####

'''
Simple auto pressing macro that presses preset buttons randomly, 
at a specified interval, for a specified duration.
'''

import pyautogui
import time
import random


duration_m = input("How long do you want to run this program for (minutes)? ")
click_interval = input("Set click interval (minutes \u00B11): ")

duration_s = float(duration_m)*60
click_interval_s = float(click_interval)*60

t_current = 0
t_cis = click_interval_s
t_start = time.time()  # because time.time() is current time, not 0

while t_current < t_start + duration_s:
    time.sleep(0.1)  # drastically decrease cpu usage, sleep for 100ms

    if t_current >= t_start + t_cis:
        random_cis = click_interval_s + random.randint(-60,60)
        t_cis += random_cis

        ct = random.randint(0,9)
        if ct == 0:
            pyautogui.keyDown('q')
            pyautogui.keyUp('q')
        elif ct == 1:
            pyautogui.keyDown('w')
            pyautogui.keyUp('w')
        elif ct == 2:
            pyautogui.keyDown('e')
            pyautogui.keyUp('e')
        elif ct == 3:
            pyautogui.keyDown('r')
            pyautogui.keyUp('r')
        elif ct == 4:
            pyautogui.keyDown('t')
            pyautogui.keyUp('t')
        elif ct == 5:
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
        elif ct == 6:
            pyautogui.keyDown('s')
            pyautogui.keyUp('s')
        elif ct == 7:
            pyautogui.keyDown('d')
            pyautogui.keyUp('d')
        elif ct == 8:
            pyautogui.keyDown('f')
            pyautogui.keyUp('f')
        else:
            pyautogui.keyDown('b')
            pyautogui.keyUp('b')
        #pyautogui.keyDown('9')
        #pyautogui.keyUp('9')
        
        random_cis_m = int(random_cis)/60
        random_cis_s = int(random_cis)%60
        t_cis_m = int(t_cis)/60
        t_cis_s = int(t_cis)%60

        print("\ntime until next click: %dm %ds" % (random_cis_m, random_cis_s))
        print("next click at: %dm %ds" % (t_cis_m, t_cis_s))
    
    t_current = time.time()
