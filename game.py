from sys import exit

def gold_room():

    print "This room is full of gold. How much do you take?"

    choice = raw_input("Write any number from 0 to 100> ") # variable
    if "0" in choice or "1" in choice: # could be 0, 1, 10, 11:19, 20, 21, 30, 31, 40, 41, 50, 51, etc.
        how_much = int(choice) # variable
    else:
        dead("Man, learn to type a number.") # launch function dead

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0) # launch system function exit
    else:
        dead("You greedy bastard!") # launch function dead

def bear_room():

    print "There is bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False # variable

    while True: # infinite loop, run until it finds a right answer
        choice = raw_input("Write 'take honey', 'taunt bear' or 'open door'> ") # variable

        if choice == "take honey": # variable check
            dead("The bear looks at you then slaps your face off.") # launch function dead
        elif choice == "taunt bear" and not bear_moved: # double variables check
            print "The bear has moved from the door. You can go thought it now."
            bear_moved = True # change the variable
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved: # variable check
            gold_room() # launch function gold_room
        else:
            print "I got no idea what that means."

def cthulhu_room():

    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee your life or eat your head?"

    choice = raw_input("Write 'flee' or 'head'> ") # variable

    if "flee" in choice: # variable check
        start() # launch function start
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room() # launch function

def dead(why):

    print why, "Good job!"
    exit(0) # launch system function exit
    # exit(0) is neutral
    # exit(1) is an error, could be a useful warning
    # exit(2) or others like exit(100) are other warnings, or different messages

def start():

    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take: left or right?"

    choice = raw_input("Write 'left' or 'right'> ") # variable

    if choice == "left": # variable check, exact
        bear_room() # launch function bear_room
    elif choice == "right": # variable check, exact
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
