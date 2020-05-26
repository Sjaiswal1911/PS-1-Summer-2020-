#the following game contains user and his journey through
#the rooms in search of gold room



from sys import exit

#function to simulate gold room
def gold_room() :

    print("This room is full of gold. How much do you take?")

    #asking user to make a choice
    choice = input(">")

    #use of try to prevent user input breaking the code
    try:
        how_much = int(choice)

    except :
        dead("Man, learn to type a number.")

    #deccdiing if the user is actually greedy or good?
    if how_much < 50 :
        print("Nice, you're not greedy. You WIN!")
        exit(0)

    else:
            dead("You greddy bastard!")

#function to simulate bear_room
def bear_room() :

    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    #variable to keep track of bear's location
    bear_moved = False

    #loop until user dies or get outside the room
    while True:

        print()
        print("Choose one of the following:")
        print("taunt bear \t open door \t take honey")
        # user chooses one of the choices
        print()
        choice = input('>')

        if choice == "take honey":
            dead("The bear slaps your face")

        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved away from the door")
            print("You can move through it.")
            bear_moved = True

        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your legs")

        elif choice == "open door" and bear_moved:
            #user leaves for gold_room and escapees  the bear
            gold_room()

        else:
            print("I got no idea what that means")

#simulates the evil ctuhulhu's room
def ctuhulhu_room():

    print("Here you see the great evil ctuhulhu.")
    print("He, it, whatever stares at you and goes insane")
    print("Do you flee for your life or eat your head?")

    #user choice determines him/her fate
    choice = input('>')

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("well that was tasty")

    else:
        #he/she is stuck in the room
        ctuhulhu_room()

#function to print the dead message and it's cause
def dead(why):
    print(why,"Good Job!")
    exit(0)

#function to start the game
def start():

    print("You are in a dark room.")
    print("There is a door to your left and right")
    print("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()

    elif choice == "right":
        ctuhulhu_room()

    else:
        print("You stumble in the room and die starving")

#initialize the game
start()
