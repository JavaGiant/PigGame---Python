# Name: Carson Smith
# pig.py
#
# Problem: This program runs the game pig, where a player competes against a computer to reach 100 points first.
#           
# Certification of Authenticity:  
#   I certify that this lab is entirely my own work.
import random
import math

def main():

    startGame = input("Would you like to start a game of pig? (yes/no) ")
    print()
    playAgain = "yes"
    while startGame == "yes":
        if startGame == "yes":
            playPig()
            print()
            startGame = input("Would you like to play again? (yes/no)")
    if startGame == "no":
        print("Okay then. :(")
    else:
        startGame = input("Would you like to start a game of pig? (yes/no)")

def playPig():

    totalPlayerPoints = 0
    totalComputerPoints = 0
    checkForTurn = "yes"
    playerTurnInput = input("Would you like to roll? ")
    print()
    playerTurnInput2 = "yes"
    while totalPlayerPoints < 100 and totalComputerPoints < 100: #Conditional to play the game
        while playerTurnInput == "yes" and checkForTurn == "yes": #Allows the player to roll until they either A) Lose their turn or B) decide not to roll
            totalPlayerPoints, checkForTurn = playerPlays(totalPlayerPoints, "yes") #Passes in player points and then the conditional whether or not the turn belongs to the player
            print("Your point total is: ", totalPlayerPoints)
            print()
            if checkForTurn == "yes":
                if totalPlayerPoints < 100: #check to make sure you did not win
                    playerTurnInput2 = input("Would you like to roll again? (yes/no) ")
                    if playerTurnInput2 == "yes":
                        playerTurnInput = "yes"
                    elif playerTurnInput2 == "no":
                        playerTurnInput = "no"
        while playerTurnInput == "no" or checkForTurn == "no": #Conditional to allow the computer to play it's turn
            print("Computer's turn...")
            totalComputerPoints = computerPlays(totalComputerPoints)
            print("The computer has: ", totalComputerPoints)
            print()
            print("The computer's turn has ended.")
            checkForTurn = "yes"
            if totalComputerPoints < 100: 
                playerTurnInput = input("Would you like to roll? (yes/no) ")
    if totalPlayerPoints >= 100: #If the player wins
        checkForTurn = "no"
        print("Congratulations! You have won!")
        print()
    if totalComputerPoints >=100: #If the computer wins 
        checkForTurn = "no"
        print("The computer has won.")
        print()
def roll(): #Function for the dice roll

    die = random.randint(1,6)
    return die

def playerPlays(totalPlayerPoints, checkForTurn): #Code for the player's turn

    turnPoints = 0
    die1 = roll()
    die2 = roll()
    if checkForTurn == "yes": #If the turn still belongs to the player. This function is called each individual roll that the player decides
        if die1 == 1 and die2 == 1:
            print("The first dice rolled: ", die1)
            print("The second dice rolled: ", die2)
            print()
            totalPlayerPoints = 0
            turnPoints = 0
            checkForTurn = "no"
            print("You lost all your points!")
            print()
        elif die1 == 1 or die2 == 1:
            print("The first dice rolled: ", die1)
            print("The second dice rolled: ", die2)
            print()
            checkForTurn = "no"
            turnPoints = 0
            print("You lost all your points for this turn!")
            print()
        else:
            print("The first dice rolled: ", die1)
            print("The second dice rolled: ", die2)
            print()
            turnPoints = die1 + die2
            totalPlayerPoints += turnPoints
    elif checkForTurn == "no":
        totalPlayerPoints += turnPoints

    return(totalPlayerPoints, checkForTurn)


def computerPlays(totalComputerPoints): #Code for the computer's turn

    turnComputerPoints = 0
    computerTurnCheck = True
    while computerTurnCheck == True and turnComputerPoints < 20:
        die1 = roll()
        die2 = roll()
        if die1 == 1 and die2 == 1:
            print("The computer's first dice rolled: ", die1)
            print("The computer's second dice rolled: ", die2)
            print()
            die1 = 0
            die2 = 0
            totalComputerPoints = 0
            turnComputerPoints = 0
            computerTurnCheck = False
        elif die1 == 1 or die2 == 1:
            print("The computer's first dice rolled: ", die1)
            print("The computer's second dice rolled: ", die2)
            print()
            die1 = 0
            die2 = 0
            turnComputerPoints = 0
            computerTurnCheck = False
        else:
            turnComputerPoints += die1 + die2
            print("The computer's first dice rolled: ", die1)
            print("The computer's second dice rolled: ", die2)
            print()

    totalComputerPoints += turnComputerPoints
    return totalComputerPoints
