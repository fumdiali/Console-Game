import time

#global gold
global boxes
gold=0
boxes=0

def game():
    print("Hello,guest!")
    uname = input("Enter a User Name:")
    print("Welcome,"+uname.capitalize()+"!")
    print()
    print("*******************")
    print("Instructions:")
    print("-------------")

    time.sleep(2)
    print("Your mission is to collect boxes on your path..")
    print("Answer all the questions and pick up 3 boxes to win!")
    choice = input("Are you ready to begin? [Y/N]")
    time.sleep(2)
    if choice == 'Y':
        #start() is our main game method
        start()
    elif choice == 'N':
        print("Okay.Bye!")
    else:
        print("Invalid choice!Enter 'Y or N' only!")

#main game method
def start():
    game_roll = True
    boxes = 0
    print("Good!Take your first step..")
    print("Your 1st step has triggered 2 questions!")
    while(game_roll):
        print("**********")
        print("Question1:")
        print("**********")
        time.sleep(3)
        q1 = input("If 6 is a half-dozen,what is 4 score and 6? ")
        if int(q1) == 86:
            print("Correct!It is 86!!")
        else:
            print("Incorrect!")
        print("**********")
        print("Question2:")
        print("**********")
        time.sleep(2)
        q2 = input("What is 1 plus 1? ")
        if int(q2) == 2:
            print("That's Correct!")
            game_roll = False
            boxes = boxes + 1
            haul = boxes

            if haul < 3:
                #convert boxes count to string for output
                print("Your Boxes: "+str(haul))
                print("You require "+str(int(3 - haul))+" more to win!")
            else:
                print("You have "+str(boxes)+"!Winner!")
        else:
            print("Incorrect!") 

    time.sleep(3)
    print("----------------------------------------------------------")
    print("Task Two Begins:")
    time.sleep(2)
    print("You're now walking down a dusty path,you hear the sound of a 'HISSSS'")
    print("There's a snake slithering to your right..")
    print("________:")
    print("|         " )
    print("| ")
    print("|_______ ")
    print("        |")
    print("        |")
    print("        |")
    snake = input("Do you a) Stamp it under-foot b) Smash it with your box [Type a/b]")
    if snake == 'a':
        print("Good job!It's a rubber snake!")
        boxes = boxes + 1
        haul = boxes

        if haul < 3:
        #convert boxes count to string for output
            print("Your Boxes: "+str(haul))
            print("You require "+str(int(3 - haul))+" more to win!")
        else:
            print("You have "+str(boxes)+"!Winner!")
    elif snake == 'b':
        print("Now why would you destroy your box???")

game()
