# basic logic for cheating hangman written in python
# we dont want to write the whole game in here, this is just experimental
# kind of like a brainstorming page. any features we want to add should start
# in this file

from time import sleep
import random

cheatword = "Dr. Rosen"

threeLongWord = ['was', 'has', 'top']
fourLongWord = ['four', 'beet','lope']
fiveLongWord = ['bleat', 'freak', 'proud']

hangmanLibrary = {3:threeLongWord, 4:fourLongWord, 5:fiveLongWord}



def slowPrint(string, delay = .1, end="\n"):
    """given a string, print each character with given delay, and given an end character"""
    for char in string:
        print(char, end='', flush=True)
        sleep(delay)
    print(end)

# user starts game

def userStart():
    slowPrint("Welcome to Hangman Unmastered!")
    slowPrint("If you do not know how to play, enter \'Teach me.\' If you do, enter nothing.")
    tutorial = str(input("Enter:"))
    while tutorial.lower() == "teach me":
        slowPrint(
            """These are the rules. At the start of each game, I will pick a word. Don't worry, I'll go easy if you ask nicely.\nEach turn, you get a chance to guess a letter. If the letter you guessed is in the word, I'll tell you. If it isn't,\nI'll tell you. I promise to tell the truth :D.""", 0.01
        )
        slowPrint('Do you understand the rules? If not, enter \'Teach me\'.', 0.01)
        tutorial = str(input("Enter:"))


# user declare guesses

def validGuess(difficulty, guesses, cheatword = "Dr. Rosen", maxG = 25):
    if type(guesses) != int:
        return [False]
    elif difficulty == "hard":
        maxG = 6
    elif difficulty == "easy" or difficulty == "impossible":
        maxG = 25
    elif difficulty == cheatword:
        maxG = 26
    if guesses > maxG or guesses <= 0:
        return [False]
    return [True, maxG]


def getGuesses(difficulty):
    if difficulty == "easy" or difficulty == "impossible":
        slowPrint("How many guesses would you like? The maximum is 25 (or is it?). ")
    elif difficulty == "hard":
        slowPrint("Due to your difficulty choice, you only get 6 or less guesses. Please choose how many guesses you would like.")
    while True:
        try:
            guesses = int(input("Guesses:"))
            validity = validGuess(difficulty, guesses)
            if validity[0]:
                slowPrint(f"Alright, {guesses} guesses it is!")
                return guesses
            else:
                if difficulty == "hard":
                    slowPrint("That is an invalid amount of guesses. Please enter a number between 1 and 6.", 0.01)
                else:
                    slowPrint("That is an invalid amount of guesses. Please enter a number between 1 and 25.", 0.01)
        except ValueError:
            slowPrint("Please enter a valid number.", 0.01)

# generate new families {"_ _ _ _": listOfWords}

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
            slowPrint("You have made a big mistake. Mwahahaha!")
        elif difficulty == cheatword:
            slowPrint("Well, since you asked SO nicely, and I promised I would go easy if you asked nicely, I'll go easy on you.\nYou have the max number of guesses, 26.")
    return difficulty

# user guess

def userGuess():
    guess = input(slowPrint("Your guess here:", .01))
    if type(guess) != int:
        input(slowPrint("Please try again.\nYour guess here:", .01))
    return guess

def main():
    userStart()
    difficulty = userDifficulty(cheatword)
    userGuesses = getGuesses(difficulty)



if __name__ == "__main__":
    main()

# cheating hangman algorithm



# choose initial word

def chooseWord(length, words):
    word = random.choice(words[length])
    return word

# user guesses letter

def letterGuess(gameStatus, chosenWord):
    pass

# print game status "_ _ _ _"

def printGameStatus(gameStatus):
    pass