import os
import sys
from random import *

class Console:
    def __init__(self):
        os.system("cls")

    def run(self):
        print("[1] Singleplayer")
        print("[2] Multiplayer")
        print("")
        choise = int(input("> "))

        if choise == 1:
            try:
                seed = int(input("What seed: "))
            except:
                seed = randrange(-9999999, 9999999)
            os.system('cls')
            print('Starting mc...')
            return {"choise": "singleplayer", "seed": seed}
        elif choise == 2:
            print("not implemented yet!")
            return {"choise": "multiplayer"}