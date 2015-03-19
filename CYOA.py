#Choose your own adventure
#By Morgan V. & (Partners names here)
#Or CYOA

#Import and value sets
import random
import math
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

# Create a window
root = Tk()
w = Label(root, text="How many fingers am I holding behind my back ?")
w.pack()

#########################  Morgan?  #########################




#########################  Stephanie  #########################





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







########################   Main Code   #####################
intro()
