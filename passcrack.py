import pyautogui
import time, sys, os

'''
time.sleep(10)
f=open("passsword.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
'''
'''from halo import Halo

spinner = Halo(text='Loading', spinner='dots')
spinner.start()
time.sleep(10)
spinner.stop()
'''

import os
import sys
import time
'''
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from halo import Halo

spinner = Halo(text='Such Spins', spinner='dots')

try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Much Colors'
    spinner.color = 'magenta'
    time.sleep(2)
    spinner.text = 'Very emojis'
    spinner.spinner = 'hearts'
    time.sleep(2)
    spinner.stop_and_persist(symbol='🦄'.encode('utf-8'), text='Wow!')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()

'''
from halo import Halo

spinner = Halo(text='This is a text that it is too long. In fact, it exceeds the eighty column standard '
                    'terminal width, which forces the text frame renderer to add an ellipse at the end of the '
                    'text. This should definitely make it more than 180!', spinner='dots', animation='marquee')

try:
    spinner.start()
    time.sleep(1)
    spinner.fail('End!')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()