# basic logic for cheating hangman written in python
# we dont want to write the whole game in here, this is just experimental
# kind of like a brainstorming page. any features we want to add should start
# in this file

from time import sleep
import random

cheatword = "Dr. Rosen"
# initialize game with needed parameters

def slowPrint(string, delay = .1, end="\n"):
    """given a string, print each character with given delay, and given an end character"""
    for char in string:
        print(char, end='', flush=True)
        sleep(delay)
    print(end)



def userStart():
    slowPrint("Welcome to Hangman Unmastered!")
    slowPrint("If you do not know to play, enter \'Teach me\'. If you do, enter nothing")
    tutorial = str(input("Enter:"))
    while tutorial.lower() == "teach me":
        slowPrint(
            """These are the rules. At the start of each game, I will pick a word. Don't worry, I'll go easy if you ask nicely.\nEach turn, you get a chance to guess a letter. If the letter you guessed is in the word, I'll tell you. If it isn't,\nI'll tell you. I promise to tell the truth :D.""", 0.01
        )
        slowPrint('Do you understand the rules? If not, enter \'Teach me\'.', 0.1)
        tutorial = str(input("Enter:"))


# user declare guesses

def validGuess(difficulty, guesses, maxG):
    if difficulty == "hard":
        while not int(guesses) or guesses > 7:
            return False
        return True
    elif difficulty == cheatword:
        pass
    else:
        while not int(guesses) or guesses > maxG:
            return False
        return True


def getGuesses(difficulty):
    if difficulty == "easy" or difficulty == "impossible":
        slowPrint("How many guesses would you like? The maximum is 26 (or is it?). ")
        guesses = (input("Guesses:"))
        while not validGuess(difficulty):
            slowPrint("That is an invalid amount of guesses. Please enter a number ")
            guesses = input("Guesses:")
    if difficulty == "hard":
        slowPrint("Due to your difficulty choice, you only get 6 or less guesses. Please choose how many guesses you would like")
        guesses = int(input("Guesses:"))
        while not validGuess(difficulty):
            slowPrint("I apologize, but if I gave you more than 6 guesses, this game wouldn't be so hard, now WOULD it?\nYou chose your own difficulty, after all!\nPlease choose a number less than 6.")
            guesses = int(input("Guesses:"))

# print game status "_ _ _ _"

def gameStatus():
    pass
# take user guess



# generate new families {"_ _ _ _": listOfWords}

threeLongWord = ['was', 'has', 'top']
fourLongWord = ['four', 'beet','lope']
fiveLongWord = ['bleat', 'freak', 'proud']

hangmanLibrary = {3:threeLongWord, 4:fourLongWord, 5:fiveLongWord}

def userDifficulty(cheatword):
    """Allows a user to choose from Easy, Hard and Impossible"""
    possDiff = ['easy','hard','impossible',cheatword]
    slowPrint("What difficulty would you like? Choose from Easy, Hard, and Impossible.")
    difficulty = input("Difficulty:").lower()
    while difficulty not in possDiff:
        slowPrint("Please try again. You may have made a typo.")
        difficulty = input("Difficulty:").lower()
    if difficulty in possDiff:
        slowPrint(f"You have chosen {difficulty}, good luck!")
        if difficulty == "impossible":
            slowPrint("You have made a big mistake. Mwahahaha!", .1)
        elif difficulty == cheatword:
            slowPrint("Well, since you asked SO nicely, and I promised I would go easy if you asked nicely, I'll go easy on you.\nYou have the max number of guesses, 27.")
    return difficulty

# choose word

def chooseWord(length, words):
    word = hangmanLibrary[length[random.choice]]


# user decide difficulty

def userDifficulty(cheatword):
    """Allows a user to choose from Easy, Hard and Impossible"""
    possDiff = ['easy','hard','impossible',cheatword]
    slowPrint("What difficulty would you like? Choose from Easy, Hard, and Impossible.")
    difficulty = input("Difficulty:").lower()
    while difficulty not in possDiff:
        slowPrint("Please try again. You may have made a typo.")
        difficulty = input("Difficulty:").lower()
    if difficulty in possDiff:
        slowPrint(f"You have chosen {difficulty}, good luck!")
        if difficulty == "impossible":
            slowPrint("You have made a big mistake. Mwahahaha!", .1)
        elif difficulty == cheatword:
            slowPrint("Well, since you asked SO nicely, and I promised I would go easy if you asked nicely, I'll go easy on you.\nYou have the max number of guesses, 27.")
    return difficulty

# user guess

def userGuess():
    guess = str(input(slowPrint("Your guess here:", .01)))
    return guess


def main():
    userStart()
    difficulty = userDifficulty(cheatword)
    maxGuesses = getGuesses(difficulty)

if __name__ == "__main__":
    main()