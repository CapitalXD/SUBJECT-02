# This is my text-based room puzzler game


"""

IMPORT SECTION -

OS for clear screen

SYS for sys.exit()

"""

import os

import sys

import time


def cls():
    os.system('cls')

def startmenu():
    cls()
    print (" Welcome To Subject02 ")
    print ("  __________________  ")
    print ("  |                |  ")
    print ("  |    SUBJECT     |  ")
    print ("  |       02       |  ")
    print ("  |________________|  ")
    print ("                      ")
    print ("    [A] Start New     ")
    print ("      [B] Load        ")
    print ("[C] Instructions/help ")
    print ("    [D] Exit Game     ")
    sm = str(raw_input("Please pick an option\n          "))
    sm = sm.lower()
    if sm == "start new" or sm == "a" or sm == "startnew" or sm == "start" or sm == "new" or sm == "a. start new" or sm == "a start new":
        stnewyorn()
    elif sm == "load" or sm == "b" or sm == "b. load" or sm == "b load":
        load()
    elif sm == "c" or sm == "instructions" or sm == "help" or sm == "instructions/help" or sm == "c instructions" or sm == "c help" or sm == "c instructions/help":
        insthelp()
    elif sm == "d" or sm =="exit" or sm == "d exit" or sm == "d exit game" or sm == "d game" or sm == "d exit game" or sm == "d. exit game":
        exitgame()
    else:
        print ("that is not an option\nPress [ENTER] to continue.")
        raw_input ("")
        startmenu()

        
def stnewyorn():
    cls()
    print ("    Do you want to begin a new game?\n(Reading instructions first is recommended) [Y/N]")
    ng = raw_input("")
    ng = ng.lower()
    if ng == "y":
        startnew()
    elif ng == "n":
        startmenu()
    else:
        print ("Please type Y or N.")
        yorn == input("Hit [ENTER] to continue")
        if yorn == "":
            stnewyorn()
        else:
            stnewyorn()


##def startnew():           
##
##
##
##def load():
##
##
##
##def insthelp():



def exitgame():
    exit = str(raw_input("Are you sure you want to quit? [Y/N]\n        "))
    exit = exit.lower()
    if exit == "y" or exit == "yes":
        sys.exit()
    elif exit == "n" or exit == "no":
        remm = str(raw_input("Return to main menu?\n     "))
        if remm == "y" or remm == "yes" or remm == "ok":
            startmenu()
        elif remm == "n" or remm == "no":
            print ("MAKE UP YOUR MIND!!!")
            muym = str(raw_input("*sigh* OK, back to the main menu now?\n     "))
            if muym == "y" or muym == "yes" or muym == "ok":
                startmenu()
            elif muym == "n" or muym == "no":
                omg = str(raw_input("OHMYGOD WHAT IS YOUR PROBLEM!?!? ARE YOU DONE?\n      "))
                if omg == "y" or omg == "yes" or omg == "ok":
                    raw_input("FINALLY. Going back to the main menu now, whether\nyou like it or not. Hit [ENTER] to continue.")
                    startmenu()
                elif omg == "n" or omg == "no":
                    print ("Nup, that's it. I'm done. Quitting now in 3...")
                    time.sleep(1)
                    print ("2...")
                    time.sleep(1)
                    print ("1...")
                    time.sleep(1)
                    print ("...and good riddance")
                    time.sleep(0.5)
                    sys.exit()
                else:
                    str (raw_input ("What? I don't get it. Hit that sexy-looking ENTER key to go back to the main menu.\n")
                    startmenu()


startmenu()








