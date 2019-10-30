from random import randint
from colorama import Fore, Back, Style
import time


print(Fore.BLUE + "\nWelcome to Snakes and Ladders!\n\nBy Jaimil Dalwadi\n\nWill you get to 100 first to achieve victory, or will the computer get there before you?\n\nThere will be fierce obstacles along the way, but also some shortcuts.\n If you land on the mouth of a snake, you will be pushed down.\n If you land at the bottom of a ladder, you can climb up.\n ")
request = str(input("Would you like to play? "))

#setting variables
userscore = 0
compscore = 0

#request possibilities
yes = ["yes" , "Yes" , " yes" , " Yes" , "YES", 'y']
no = ["no" , "No" , " no" , " No" , "NO",'n']

#different snake possibilities
snakemouth = [54,90,99]
snakeass = [19,48,77]

#different ladder possibilities
ladderbottom = [9,40,67]
laddertop = [32,64,86]
if request in no:
    print("Okay, thanks for trying this")

#error statement if player doesn't answer properly
while request not in no and request not in yes:
    request = str(input("Error, please state yes or no: "))
    if request in no:
        print("Okay, thanks for trying this")
#functions
def checkSnakes():
    global userscore
    global compscore
    if userscore in snakemouth:
        userscore = snakeass[snakemouth.index(userscore)]
        print("OH MAN! You landed on a snake, you go to spot", str(userscore))
    if compscore in snakemouth:
        compscore = snakeass[snakemouth.index(compscore)]
        print("OH YES! Computer landed on a snake, it goes to spot", str(compscore))
def checkLadders():
    global userscore
    global compscore
    if userscore in ladderbottom:
        userscore = laddertop[ladderbottom.index(userscore)]
        print("OH YES! You landed on a ladder, you go to spot", str(userscore))
    if compscore in ladderbottom:
        compscore = laddertop[ladderbottom.index(compscore)]
        print("OH NO! Computer landed on a ladder, it goes to spot", str(compscore))

def rollDice():
    global dice1
    dice1 = randint(1,6)
    global dice2
    dice2 = randint(1,6)

#opening while loop for running the game when the player wants to play
while request in yes:
    userscore = 0
    compscore = 0
    #main while loops with code to actually run the game
    while userscore < 100 and compscore < 100:
        print("\n------------------------------------------------------------","\n")
        #code for the player/user
        rollDice()
        print("Your first die showed", str(dice1), "and your second die showed", str(dice2), "\n")
        userscore = userscore + dice1 + dice2
        if userscore == 100:
            print("Oh YES! You landed on 100! YOU  WON! Computer lost!\n")
            break;
        elif userscore > 100:
            print("Oh man! Your piece can't go past 100, so it stays at the same spot.\n")
            userscore = userscore - (dice1 + dice2)
        print("Your piece is at", str(userscore),"\n")
        #code for the computer
        rollDice()
        print("Computer's first die showed", str(dice1), "and the second die showed", str(dice2),"\n")
        compscore = compscore + dice1 + dice2
        if compscore == 100:
            print("Oh man! The computer landed on 100! The COMPUTER WON! You lose....\n")
            break;
        elif compscore > 100:
            print("Oh yes! The computer can't go past 100, so it stays on the same spot.\n")
            compscore = compscore - (dice1 + dice2)
        print("Computer piece is at", str(compscore),"\n")
        checkSnakes()
        checkLadders()
        print("------------------------------------------------------------","\n")
        time.sleep(4)
    #keep playing or not
    request = str(input("Would you like to play again? "))
    if request in no:
        print("Okay, thanks for playing! Be sure to play again after!")
    #error statement if player doesn't answer properly
    while request not in no and request not in yes:
        request = str(input("Error, please state yes or no: "))
        if request in no:
            print("Okay, thanks for playing! Be sure to play again after!")

    
