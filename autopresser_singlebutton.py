#####auto-clicker macro v1.0#####

'''
Simple auto click macro that clicks a single spot (where cursor is located)
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
        #pyautogui.click()
        pyautogui.keyDown('g')
        pyautogui.keyUp('g')
        
        random_cis_m = int(random_cis)/60
        random_cis_s = int(random_cis)%60
        t_cis_m = int(t_cis)/60
        t_cis_s = int(t_cis)%60

        print("\ntime until next click: %dm %ds" % (random_cis_m, random_cis_s))
        print("next click at: %dm %ds" % (t_cis_m, t_cis_s))
    
    t_current = time.time()
