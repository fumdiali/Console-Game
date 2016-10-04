# simple game to demonstrate dice roll game
import random

print("This is my Dice Roll game")
print("--------------------------")
uname = input("Enter your chosen User Name:")
print("Welcome,"+uname.capitalize()+". Roll a 6 to win!")
'''
def start_game():
    game()

def game():
'''
game_on = True

while game_on:
    print("Press [ENTER] to roll..[type 'q' to quit]")
    keyy = input()
    
    if keyy == 'q':
        game_on = False
        print("Thanks for playing!")
    else:    

        roll = random.randint(1,6)
        if roll == 1:
            print("______ ")
            print("|     |")
            print("|  O  |")
            print("|_____|")
            print("You rolled a 1!")
        if roll == 2:
            print("______ ")
            print("|     |")
            print("| OO  |")
            print("|_____|")
            print("You rolled a 2!")
        if roll == 3:
            print("______ ")
            print("|  O  |")
            print("|  O  |")
            print("|__O__|")
            print("That's a 3!")
        if roll == 4:
            print("______ ")
            print("| O O |")
            print("|     |")
            print("|_O_O_|")
            print("You got a 4!")
        if roll == 5:
            print("______ ")
            print("| O O |")
            print("|  O  |")
            print("|_O_O_|")
            print("You rolled a 5!")
        if roll == 6:
            print("______ ")
            print("| O  O|")
            print("| O  O|")
            print("|_O__O|")
            print("High number 6! You win!")
            game_on = False
'''
rewind = input("Go Again? [Y/N]")
if rewind == 'Y':
    start_game()
elif rewind == 'N':
    print("Thanks for playing!")
else:
    print("I don't understand")
    '''
