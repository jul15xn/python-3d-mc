import os
import sys

class Console:
    def __init__(self):
        os.system("cls")

    def run(self):
        print("[1] Singleplayer")
        print("[2] Multiplayer")
        print("")
        choise = int(input("> "))

        if choise == 1:
            seed = int(input("What seed: "))
            os.system('cls')
            print('Starting mc...')
            return {"choise": "singleplayer", "seed": seed}
        elif choise == 2:
            print("not implemented yet!")
            return {"choise": "multiplayer"}