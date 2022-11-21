"""
#### ========// README // ======= ##
# Created on Tue Nov 15 2022
#@author: angela

# For this script to work correctly, the following conditions must be in place:
#   1. The Messari and Encode tables must be opened in Chrome                           // (for shortcuts to work)
#   2. The Messari tab must be to the left of the Encode tab                            // (so the order of copying and pasting is correct)
#   3. Hide all fields in the Messari tab apart from: date, amount, investors, stages   // (So the order of copying is correct)
#   4. Filter the Messari records so only the ones to be copied are in view             // (not exactly necessary but helps avoid mistakes)
#   5. In the Encode table, the input view must be active                               // (so data is pasted in the right place)
#   6. Before you start the script, ensure the correct starting cells are selected:
#           - Messari tab -- topleft-most cell selected
#           - Encode tab -- left-most cell of the line the data will be added from
#   7. When the script is activated with the enter key, go to the Messari tab and wait
#
# Top tips:
#   + The script will automatically add new records into the Encode table
#   + Do not touch your keyboard or mouse/trackpad when the script begins
#

## =============================== ##
"""

import pyautogui
import time

print('START')
time.sleep(1)

## Wait for user input
i = int(input('\nHow many lines of records are to be copied across?\n'))
time.sleep(1)

## Wait for user to be ready
enterkey = input('\nPlease ensure you have read the README section in the source code. \nWhen you are ready, press enter to start the script.\nYou will have 5 seconds to change the window to the Messari tab after you press enter.')

## Countdown to script starting
time.sleep(1); print('5')
time.sleep(1); print('4')
time.sleep(1); print('3')
time.sleep(1); print('2')
time.sleep(1); print('1')

x = 0
for x in range(i):
    n = 0
    for n in range(5):                          #number of cells per line to copy over
        #print(x);print(n)
        pyautogui.hotkey('command', 'c')                            #copy from first tab
        pyautogui.press('right')                                    #move to next cell
        pyautogui.hotkey('command', 'option', 'right')
        pyautogui.hotkey('command', 'v')                            #paste to Encode tab
        pyautogui.press('right')                                    #move to next cell
        pyautogui.hotkey('command', 'option', 'left')               #return to Missari table
        n = n+1
        
    ## make new record for encode table
    pyautogui.hotkey('command', 'option', 'right')                  #return to Encode table
    pyautogui.press(['down','left', 'left', 'left', 'left'])        #Return to leftmost cell
    pyautogui.hotkey('shift', 'enter')                              #create new record below
    pyautogui.press('esc')                                          #exit from typing
    
    ## reset Messari table
    pyautogui.hotkey('command', 'option', 'left')                   #return to Encode table
    pyautogui.press(['down','left', 'left', 'left', 'left'])        #Return to leftmost cell
    
    
    x = x+1 #increment record number
    
else:
    print('END')