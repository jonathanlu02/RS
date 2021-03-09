#######key slider macro#######
'''
Takes in jumbled commands containing strings of "left", "right", "up", "down"
and executes them based on their order.

Uses randomness in how fast the slider boxes move to avoid auto-detection while
mimicking human like behavior.

Instructions:

For Alt1. Set Instruction list (ON), Flip directions (ON). Press Guide
and copy/paste the instructions once prompted. Will automatically solve
the slide puzzle for you without any other input required by pressing arrow
keys automatically. 


NOTE: once program starts initiating (countdown), switch back to RS tab
for the key presses to work. 
'''

import pyautogui
import time
import random

repeat = True

while repeat:
    print("Copy & paste the commands here (enter x to quit): ")

    # to read multi-lines in shell
    lines = []
    count = 0
    break_flag = False
    
    while True:
        line = input()
        if count == 0 and (line == "x" or line == "X"):
            break_flag = True
            break
        if line:
            lines.append(line)
        else:
            break
        count += 1
    txt = '\n'.join(lines)


    if break_flag:
        break
    

    recompiled_cmds = []

    valid_cmds = ["up","down","left","right"]
    cmd = ""

    for char in txt.lower():
        cmd = cmd + char
        if (valid_cmds[0] in cmd):
            recompiled_cmds.append(valid_cmds[0])
            cmd = ""
        elif (valid_cmds[1] in cmd):
            recompiled_cmds.append(valid_cmds[1])
            cmd = ""
        elif (valid_cmds[2] in cmd):
            recompiled_cmds.append(valid_cmds[2])
            cmd = ""
        elif (valid_cmds[3] in cmd):
            recompiled_cmds.append(valid_cmds[3])
            cmd = ""


    ## print(recompiled_cmds)
    print("total number of steps: " + str(len(recompiled_cmds)))

    print("\nProgram will start in: ")
    for x in range(3,0,-1):
        print(x)
        time.sleep(1)

    # feel free to change times to your liking. Default is set to 10-30ms
    for key in recompiled_cmds:
        r = random.randint(10,30)/10000.0 
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
        time.sleep(r)


    #response = input("Would you like to repeat (y/n)?: ")
    #if (response.lower() != "x"):
        #repeat = False


