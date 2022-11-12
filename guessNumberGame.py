# A simple guessing the number game

# Imports
from random import randint


# Functions
# Welcome message
def welcomeMessage():
    print("\nWelcome to Guess the Number Game\nI'm thinking a number between 1 to 10.\nGuess what it is.")


# Hold a number
def holdNum():
    holdedNum = randint(1, 10)
    return holdedNum


# Guess the number
def guessNum():
    guessedNum = 0
    while 1 > guessedNum or 10 < guessedNum:
        try:
            guessedNum = int(input("\nPlease enter a number between 1 to 10: "))
        except ValueError:
            print("That wasn't an integer :(")
    return guessedNum


# Ask if the user wants to play again
def askStart():
    answerOfAskStart = ""
    while True:
        answerOfAskStart = str(input("\nDo you want to play again?(Y/N) ")).lower().strip().replace(" ", "")
        if answerOfAskStart == "y" or answerOfAskStart == "yes":
            print("Here we go again.")
            gameCore()
        elif answerOfAskStart == "n" or answerOfAskStart == "no":
            print("\nThat's too bad. Hope we see you again.")
            exit()
        else:
            print("Please enter either Y or N.")
            continue


# Call hold number and guess number functions. Compare the result and output it.
def gameCore():
    holdedNum = holdNum()
    guessedNum = guessNum()
    if guessedNum == holdedNum:
        print("\nWow! You actually guessed right. The number I tought was {0}.".format(holdedNum))
    else:
        print("\nSorry. You couldn't guess right. The number I tought was {0}.".format(holdedNum))
    askStart()


# Execute the game
welcomeMessage()
gameCore()
