# A simple guessing the number game

# Imports
from random import randint


# Functions
# Welcome message
def welcomeMessage():
    print("\nWelcome to Guess the Number Game\nI'm thinking a number between 1 to 100.\nGuess what it is.")


# Entry of guessed number
def guessNum():
    guessedNum = 0
    while 1 > guessedNum or 100 < guessedNum:
        try:
            guessedNum = int(input("\nPlease enter a number between 1 to 100: "))
        except ValueError:
            print("That wasn't an integer :(")
    return guessedNum


# Core of the game
def gameCore():
    holdedNum = randint(1, 100)  # The target number gets holded
    playerWon = False
    guessCount = 0  # Create a counter for guess attempts
    while playerWon == False:  # Loop till player guesses right
        guessedNum = guessNum()
        guessCount += 1
        if guessedNum == holdedNum:  # Check if the user's guess is right
            print("\nWow! You guessed right, the number I tought was {1}. It took {0} attempt(s).".format(guessCount, holdedNum))
            playerWon = True
        elif guessedNum < holdedNum:  # Check if the user's guess is low
            print("\nSorry. You couldn't guess right. The number I hold is higher.")
        elif guessedNum > holdedNum:  # Check if the user's guess is high
            print("\nSorry. You couldn't guess right. The number I hold is lower.")

    askStart()


# Ask if the user wants to play again
def askStart():
    answerOfAskStart = ""
    while True:
        answerOfAskStart = str(input("\nDo you want to play again?(Y/N) ")).lower().replace(" ", "")
        if answerOfAskStart == "y" or answerOfAskStart == "yes":
            print("Here we go again.")
            gameCore()
        elif answerOfAskStart == "n" or answerOfAskStart == "no":
            print("\nThat's too bad. Hope we see you again.")
            exit()
        else:
            print("Please enter either Y or N.")
            continue


# Execute the game
welcomeMessage()
gameCore()
