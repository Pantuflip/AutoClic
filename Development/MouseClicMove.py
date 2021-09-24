# -*- coding: utf-8 -*-

# pip install keyboard
# pip install pyautogui
# pip install auto-py-to-exe
# if the program doesnt run you need to install the previous libreries.

import keyboard
import pyautogui as pa
import random
import time # libreria de tiempo´
import schedule

def moveMouse():
    x=random.randint(50, 1810)
    y= random.randint(50, 900)
    if x>50 and x <1810:
        if y>50 and y <900:
            pa.moveTo(x, y)
            pa.click()
            print(pa.position()) # posicion del mouse

def run():
    print(pa.size()) # tamaño pantalla
    print(pa.position()) # posicion del mouse

    schedule.every(30).seconds.do(moveMouse)

    while not keyboard.is_pressed('q'):
        schedule.run_pending()

if __name__ == '__main__':
    run()
