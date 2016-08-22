#-*- coding: utf-8 -*-



# This is my text-based room puzzler game


"""

IMPORT SECTION -

OS for clear screen

SYS for sys.exit()

"""

import os

import sys

import time

## 
##   TYPING EFFECT!
##

l1  = " Welcome To Subject02 \n"
l2  = "  __________________  \n"
l3  = "  |                |  \n"
l4  = "  |     SUBJECT    |  \n"
l5  = "  |       02       |  \n"
l6  = "  |________________|  \n"
l7  = "\n"
l8  = "    [A] Start New     \n"
l9  = "      [B] Load        \n"
l10 = "[C] Instructions/help \n"
l11 = "    [D] Exit Game     \n"


inst1 = "Welcome to Subject02!\n"
inst2 = "This game is a classic text-based\n"
inst3 = "game. No images, just words to\n"
inst4 = "guide you through your quest.\n"
inst5 = "Subject02 is about you, a teenage boy\n"
inst6 = "and your adventures trying to escape\n"
inst7 = "from a top-secret scientific research\n"
inst8 = "facility.\n"
inst9 = "\n"
inst10= "In Subject02 you will be placed\n"
inst11= "in all sorts of different situations. \n"
inst12= "To act, you must type commands, such\n"
inst13= "as 'Dig' or 'Swim'. If your command\n"
inst14= "is mis-spelled, or not an available\n"
inst15= "option, you will see an error message\n"
inst16= "appear on your screen - e.g. \"<command>\n"
inst17= " is not an available option.\" Or \"you\n"
inst18= "can't select <command> now. Please try\n"
inst19= "again.\" Commands are not case-sensitive.\n"
inst20= "\n"
inst21= "At any time during the course of the game,\n"
inst22= "you may type , \"H\", and a list of possible\n"
inst23= "(but not all) commands will be shown. This\n"
inst24= "is a last-resort, and is suggested to only\n"
inst25= "be used when you have been stuck for an\n"
inst26= "extended period of time.\n"

def insttype():
    type(inst1)
    type(inst2)
    type(inst3)
    type(inst4)
    type(inst5)
    type(inst6)
    type(inst7)
    type(inst8)
    type(inst9)
    type(inst10)
    type(inst11)
    type(inst12)
    type(inst13)
    type(inst14)
    type(inst15)
    type(inst16)
    type(inst17)
    type(inst18)
    type(inst19)
    type(inst20)
    type(inst21)
    type(inst22)
    type(inst23)
    type(inst24)
    type(inst25)
    type(inst26)


def type(line):
    for char in line:
        time.sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

def cls():
    os.system('cls')

def startmenutype():
    cls()
    type(l1)
    type(l2)
    type(l3)
    type(l4)
    type(l5)
    type(l6)
    type(l7)
    type(l8)
    type(l9)
    type(l10)
    type(l11)
    smoptions()


    
def smoptions():
    sm = str(raw_input("Please pick an option\n          "))
    sm = sm.lower()
    if sm == "start new" or sm == "a" or sm == "startnew" or sm == "start" or sm == "new" or sm == "a. start new" or sm == "a start new":
        stnewyorn()
    elif sm == "load" or sm == "b" or sm == "b. load" or sm == "b load":
        load()
    elif sm == "c" or sm == "instructions" or sm == "help" or sm == "instructions/help" or sm == "c instructions" or sm == "c help" or sm == "c instructions/help":
        insttype()
    elif sm == "d" or sm =="exit" or sm == "d exit" or sm == "d exit game" or sm == "d game" or sm == "d exit game" or sm == "d. exit game":
        exitgame()
    else:
        print ("that is not an option\nPress [ENTER] to continue.")
        raw_input ("")
        startmenu()

def startmenu():
    cls()
    print(" Welcome To Subject02 ")
    print("  __________________  ")
    print("  |                |  ")
    print("  |     SUBJECT    |  ")
    print("  |       02       |  ")
    print("  |________________|  ")
    print("\n")
    print("    [A] Start New     ")
    print("      [B] Load        ")
    print("[C] Instructions/help ")
    print("    [D] Exit Game     ")
    smoptions()
    
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
        yorn = str(raw_input("Please type Y or N.\n     "))
        if yorn == "y" or yorn == "yes":
            print("OK, starting now.")
            time.sleep(0.5)
            startnew()
        elif yorn == "n" or yorn == "no":
            print("OK, going back to main menu now.")
            time.sleep(1)
            startmenu()

##def startnew():           
##def load():
def insthelp():
    print("Welcome to Subject02!\n This game is a classic text-based\n game. No images, just words to \n guide you through your quest. \n Subject02 is about you, a teenage boy\n and your adventures trying to escape\n from a top-secret scientific research\n facility.\n \n In Subject02 you will be placed\n in all sorts of different situations.\n To act, you must type commands, such\n as 'Dig' or 'Swim'. If your command\n is mis-spelled, or not an available\n option, you will see an error message\n appear on your screen - e.g. \"<command>\n is not an available option.\" Or \"you\n can't select <command> now. Please try\n again.\" Commands are not case-sensitive.\n \n At any time during the course of the game,\n you may type , \"H\", and a list of possible\n (but not all) commands will be shown. This\n is a last-resort, and is suggested to only\n be used when you have been stuck for an\n extended period of time.\n ")
    x = false
    
def idkmm():
    str (raw_input ("What? I don't get it.\nHit that sexy-looking ENTER key\nto go back to the main menu.\n"))
    print ("Going back in 1 second...")
    time.sleep(1)
    startmenu(1)

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
                    time.sleep(0.5)
                    startmenu()
                elif omg == "n" or omg == "no":
                    print ("Nup, that's it. I'm done. Quitting now in 3...")
                    time.sleep(1)
                    print ("2...")
                    time.sleep(1)
                    print ("1...")
                    time.sleep(1)
                    print ("...and good riddance")
                    time.sleep(1.5)
                    sys.exit()
                else:
                    idkmm()
            else:
                idkmm()
        else:
            idkmm()
    else:
        idkmm()


startmenutype()








