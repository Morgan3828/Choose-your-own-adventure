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

def thirdchoiceA():
    """Third decision"""
    # User Info then third choice
    messagebox.showinfo("Story Explaination",
                        "You chose to enter. "+
                        "That's good cause it means your not a wuss.")
    messagebox.showinfo("Story Explaination",
                        "As you open the door your shocked & puzzled "+
                        "for a moment. You step inside and outside of "+
                        "the door comparing the inside to the outside "+
                        "to come to a conclusion and mutter to yourself "+
                        "'It's Bigger on the Inside!' "+
                        "Will you enter or go elsewhere?")
def thirdchoiceAR():
    
    thirdchoice = simpledialog.askinteger("Story Decision",
                            "1 to enter the box and take a look at the center"+
                            ", 2 to walk out:")

    if thirdchoice == 1:
        fourthchoiceA()
        fourthchoiceAR()
    elif thirdchoice == 2:
        fourthchoiceB()
        fourthchoiceBR()
    else:
        thirdchoiceAR()

def thirdchoiceB():
    """Third decision"""
    # User Info then third choice
    messagebox.showinfo("Story Explaination",
                        "You climb over the box, because it's faster than"+
                        " going round the long way, to the next sidewalk."+
                        " When you jump down, you look up and find the dry"+
                        " cleaners, because your mom asked you to pick up"+
                        " her clothes. As you walk in, right away, you"+
                        " realize that there's nobody around. As you move"+
                        " you stumble and accidentally hit the panel of"+
                        " one of the dryers. when you get up to see what"+
                        " you did, and you see that the panel opened to"+
                        " reveal a button. It looks very shiny...")
    
    messagebox.showinfo("Story Explaination",
                        "1 to Press the Button"+
                        ", or "
                        "2 to Close the panel and Wait:")

def thirdchoiceBR():
    
    thirdchoice = simpledialog.askinteger("Story Decision",
                                          "1 to press the button"+
                                          ", 2 for NOT pressing the button:")
    if thirdchoice == 1:
        fourthchoiceC()
        fourthchoiceCR()
    elif thirdchoice == 2:
        fourthchoiceD()
        fourthchoiceDR()
    else:
        thirdchoiceAR()

def fourthchoiceA():
    """Fourth decision"""
    # User Info, then Fourth choice
    messagebox.showinfo("Story Explaination",
                        "You enter the Box.")
    messagebox.showinfo("Story Explaination",
                        "After walking to the center of this...bigger"+
                        " on the inside blue box, you notice the center"+
                        " panel has an astronomical amount of buttons"+
                        " with very weird looking round symbols on what"+
                        " to you looks like a computer screen. You go"+
                        " crazy with them and hit as many buttons as you"+
                        " can, and as fun as it is, you get nervous after"+
                        " there's a lot of flashing and the whole place"+
                        " shakes with the sound of a wheezing groan. For"+
                        " some reason it seems familiar to you, like"+
                        " you've seen or heard somewhere before. When"+
                        " you get tired and everything stops shaking"+
                        " again, you stand up and walk out the door to"+
                        " see that your in a plain, but when you look up"+
                        " shear terror and shock clings to you as you see"+
                        " a T-rex that's looking right at you now."+
                        "   Do you run away from the box and make"+
                        " a break for the trees, or do you dive into the"+
                        " Box again?")
def fourthchoiceAR():
    
    fourthchoice = simpledialog.askinteger("Story Decision",
                            "1 to RUN THE HELL AWAY"+
                            " or, "+
                            "2 to Dive back into the box:")

    if fourthchoice == 1:
        fifthchoiceA()
        fifthchoiceAR()
    elif fourthchoice == 2:
        fifthchoiceB()
        fifthchoiceBR()
    else:
        fourthchoiceAR()

def fourthchoiceB():
    """Fourth decision"""
    # User Info, then Fourth choice
    messagebox.showinfo("Story Explaination",
                        "You walk out of the box.")
    messagebox.showinfo("Story Explaination",
                        "What do you want to do now?")
def fourthchoiceBR():
    
    fourthchoice = simpledialog.askinteger("Story Decision",
                            "1 to Book it, and run home"+
                            " or, "+
                            "2 to Climb over the box and make your way to"+
                            " the other sidewalk:")

    if fourthchoice == 1:
        fifthchoiceA()
        fifthchoiceAR()
    elif fourthchoice == 2:
        fifthchoiceB()
        fifthchoiceBR()
    else:
        fourthchoiceAR()

def fourthchoiceC():
    """Fourth decision"""
    # User Info, then Fourth choice, 2nd set
    messagebox.showinfo("Story Explaination",
                        "You pushed the Button...HA")
    messagebox.showinfo("Story Explaination",
                        "When you press the button, the washers fold away to"+
                        " reveal an elevator. Do you take the elevator?")
def fourthchoiceCR():
    
    fourthchoice = simpledialog.askinteger("Story Decision",
                            "1 to Take the elevator up"+
                            " or, "+
                            "2 to Press the button again, close the panel and"+
                            " wait:")

    if fourthchoice == 1:
        fifthchoiceC()
        fifthchoiceCR()
    elif fourthchoice == 2:
        fifthchoiceD()
        fifthchoiceDR()
    else:
        fourthchoiceCR()

def fourthchoiceD():
    """Fourth decision"""
    # User Info, then Fourth choice, 2nd set
    messagebox.showinfo("Story Explaination",
                        "")
    messagebox.showinfo("Story Explaination",
                        "")
def fourthchoiceDR():
    
    fourthchoice = simpledialog.askinteger("Story Decision",
                            "1 "+
                            " or, "+
                            "2 :")

    if fourthchoice == 1:
        fifthchoiceD()
        fifthchoiceDR()
    elif fourthchoice == 2:
        fifthchoiceD()
        fifthchoiceDR()
    else:
        fourthchoiceDR()



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
# It works by an else statement. Just look at my code for an example.


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

########################  Code Start  #####################
begin()


