# Choose your own adventure
# By Morgan V. & (Partners names here)
# Or CYOA

#Import and value sets
import random
import math
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

# Create a window
root = Tk()
w = Label(root, text="Choose your own adventure")
w.pack()

#########################  Morgan  #########################
def begin():
    """First Decision"""
    # User Info then first choice
    messagebox.showinfo("Hello!", "This is the beginning of YOUR story!")
    firstchoice = simpledialog.askinteger("First choice:",
                                        "Your walking home, and there are 2 paths."+
                                        " Which do you take?"+
                                        " 1 for the shady alley"+
                                        ", 2 for the sidewalk")
    if firstchoice == 1:
        secondchoiceA()
        secondchoiceAR()
    elif firstchoice == 2:
        secondchoiceB()
        secondchoiceBR()
    else:
        begin()

def secondchoiceA():
    """Second decision"""
    # User Info then second choice
    messagebox.showinfo("Story Explaination",
                        "You chose the Shady Alley way."+
                        " In that case this'll be fun.")
    messagebox.showinfo("Story Explaination",
                        "You walk down the alley and you see a"+
                        " blue box with a sign on top labeled"+
                        " 'POLICE PUBLIC CALL BOX'."+
                        " Will you enter the Police box, or"+
                        " continue to walk elsewhere?")
def secondchoiceAR():
    
    secondchoice = simpledialog.askinteger("Story Decision",
                            "1 to enter the box"+
                            ", 2 to go elsewhere:")
    if secondchoice == 1:
        thirdchoiceA()
        thirdchoiceAR()
    elif secondchoice == 2:
        thirdchoiceB()
        thirdchoiceBR()
    else:
        secondchoiceAR()



#########################  Jacob  #########################

def secondchoiceB():
    """Second decision"""
    # User Info then third choice
    messagebox.showinfo("Story Explaination",
                        "You chose the sidewalk, "+
                        "like a rational, sane person would ")
    messagebox.showinfo("Story Explaination",
                        "")

def secondchoiceBR():
    
    secondchoice = simpledialog.askinteger("Story Decision",
                            "1 to enter the box"+
                            ", 2 to go elsewhere:")
    if secondchoice == 1:
        thirdchoiceA()
        thirdchoiceAR()
    elif secondchoice == 2:
        thirdchoiceB()
        thirdchoiceBR()
    else:
        secondchoiceAR()
# Note for Jacob: the "R" next to the "A & B" are for a restart setting.
# It's for in the case that the user chooses another number other than 1 or 2

####################  HundredVisions Guy  #################
def intro():
    """ initial decision to be made    """
    # Add some story flair
    messagebox.showinfo("Welcome", "Beginning of the story")
    # User must decide
    choice = simpledialog.askinteger("Choice",
                                    "Do you choose 1, 2, or 3?")
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        intro()

########################   Code Start  #####################
begin()


