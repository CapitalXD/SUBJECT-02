# This is my text-based room puzzler game

def startmenu():
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
    strtmnu = str(input("Please pick an option"))
    strtmnu = strtmnu.lower
    if strtmnu == "start new" or strtmnu == "a" or strtmnu == "startnew" or strtmnu == "start" or strtmnu == "new" or strtmnu == "a. start new":
        stnewyorn()
    else:
        print ("that is not an option\nPress [ENTER] to continue.")
        input ("")
        startmenu()

def stnewyorn():
    print ("    Do you want to begin a new game?\n(Reading instructions first is recommended) [Y/N]")
    ng == input("")
    ng == ng.lower
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

#def startnew():
    


startmenu()
