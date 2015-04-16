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
    messagebox.showinfo("Hello!", "This is the beginning of your story!")
    1stchoice = simpledialog.askinteger("First choice:",
                                        "Your walking home, and there are 2 paths.",
                                        "Which do you take?",
                                        "1 for the shady alley",
                                        "2 for (TO BE DECIDED)")
    if 1stchoice == 1:
        2ndchoiceA()
    elif 1stchoice == 2:
        2ndchoiceB()
    else:
        begin()

def 2ndchoiceA():
    messagebox.showinfo("You chose the Shady Alley way."
                        ,"In that case this'll be fun.")
    messagebox.showinfo("You walk down the alley and you see a",
                        " blue box with a sign on top labeled",
                        " 'POLICE PUBLIC CALL BOX'.",
                        "",
                        "Will you enter the Police box, or

#########################  Jacob  #########################




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







########################   Main Code 1  #####################
begin()


