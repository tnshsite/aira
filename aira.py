from os import *
from time import *

dev_mode = 0

def gamestart():
    print("Welcome to Aira!\n")
    print("Would you like to start? (Y/n)")
    start = input()

    if start == "Y" or start == "y":
        system("clear")


gamestart()
