from random import randint

#different possibilities of inputs
one = ["Rock", "rock", " rock", " Rock", "ROCK"]
two = ["Paper", "paper"," paper", " Paper","PAPER"]
three = ["Scissors","scissors", " scissors", " Scissors", "SCISSORS"]
computerchoice = ["Rock", "Paper", "Scissors"]
yes = ["yes" , "Yes" , " yes" , " Yes" , "YES", 'y']
no = ["no" , "No" , " no" , " No" , "NO",'n']

#fancy gameplay
print("|>>>>>>>>-------------<<<<<<<<<|" + "\n" + "WELCOME TO ROCK, PAPER, SCISSORS\n" + "Created by: Jaimil Dalwadi\n" + "|>>>>>>>>-------------<<<<<<<<<|")
#getting input on whether they want to play or not
request = str(input("Would you like to play?\n"))

#score variables initialized
playercounter = 0
computercounter = 0

#what to do if player doesn't want to play
if request in no:
    print("Okay, thanks for trying this")

#error statement if player doesn't answer properly
while request not in no and request not in yes:
    request = str(input("Error, please state yes or no: "))
    if request in yes:
        break;
    elif request in no:
        print("Okay, thanks for trying this")
        break;
#while the player wants to play, what the program should do
while request in yes:
    #get player's choice for rock paper or scissors
    play = str(input("Rock, Paper, or Scissors?\n"))
    #error statement if the player doesn't choose properly
    while play not in one and play not in two and play not in three:
        play = str(input("Error, please choose rock, paper, or scissors?\n"))
        if play in one or play in two or play in three:
            break;
    #setting a computer choice randomly, 1 being rock, 2 being paper, 3 being scissors
    computer = randint(1,3)
    #setting integer values for the player choice so it is easier to check who won
    if play in one:
        play = 1
    elif play in two:
        play = 2
    elif play in three:
        play = 3
    #shows the player what the computer chose
    print("The computer chose: " + computerchoice[computer - 1])
    #different possible outcomes of the game
    if play == computer:
        playercounter += 0;
        print("\nOH MAN! It's a TIE! Play again!\n")
    elif play == 1 and computer == 3 or play == 2 and computer == 1 or play == 3 and computer == 2:
        playercounter += 1;
        print("\nCONGRATULATIONS! You WON! Want to test your luck again?\n")
    else:
        computercounter += 1;
        print("\nAwh man! You LOST! Be sure to try again.\n")
    print("Player Score: " + str(playercounter) + '\n' + "Computer Score: " + str(computercounter))
    #asks if they want to play again
    request = str(input("Would you like to play again?\n"))
    if request in no:
        print("Thanks for playing, be sure to run it again another time")
        break;
    while request not in no and request not in yes:
        request = str(input("Error, please state yes or no: "))
        if request in yes:
            reset = str(input("Would you like to reset the score?\n"))
            if reset in yes:
                computercounter = 0
                playercounter = 0
            elif reset in no:
                computercounter = computercounter
                playercounter = playercounter
            while reset not in no and reset not in yes:
                reset = str(input("Error, please state yes or no: "))
                if reset in yes:
                    computercounter = 0
                    playercounter = 0
                    break;
                elif reset in no:
                    computercounter = computercounter
                    playercounter = playercounter
                    break;
        elif request in no:
            print("Thanks for playing, be sure to run it again another time")
            break;
    #asks if they want to reset the score:
    reset = str(input("Would you like to reset the score?\n"))
    if reset in yes:
        computercounter = 0
        playercounter = 0
    elif reset in no:
        computercounter = computercounter
        playercounter = playercounter
    while reset not in no and reset not in yes:
        reset = str(input("Error, please state yes or no: "))
        if reset in yes:
            computercounter = 0
            playercounter = 0
            break;
        elif reset in no:
            computercounter = computercounter
            playercounter = playercounter
            break;
        
        
