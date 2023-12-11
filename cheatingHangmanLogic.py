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

# utlitiy print function

def slowPrint(string, delay = .1, end="\n"):
    """given a string, print each character with given delay, and given an end character"""
    for char in string:
        print(char, end='', flush=True)
        sleep(delay)
    print(end)

# tutorial

def tutorial():
    slowPrint("Welcome to Hangman Unmastered!")
    slowPrint("If you do not know how to play, enter \'Teach me.\' If you do, enter nothing.")
    tutorial = str(input("Enter:"))
    while tutorial.lower() == "teach me":
        slowPrint(
            """These are the rules. At the start of each game, I will pick a word. Don't worry, I'll go easy if you ask nicely.\nEach turn, you get a chance to guess a letter. If the letter you guessed is in the word, I'll tell you. If it isn't,\nI'll tell you. I promise to tell the truth :D.""", 0.01
        )
        slowPrint('Do you understand the rules? If not, enter \'Teach me\'.', 0.01)
        tutorial = str(input("Enter:"))

# validates if guess number is valid

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

# user declares guess amount

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

# user set length

def userSetLength():
    length = -1
    while type(length) is not int or (length > 8 or length < 2):
        try: 
            slowPrint("How long can my word be?\nEnter a number between 2 and 8:", 0.1, "")
            length = int(input())
        except:
            continue
    return length

# choose initial family

def initFamily(length):
    words = open("words_alpha.csv", 'r').read().split('\n')
    # print(words)
    key = "_" * length
    value = [word for word in words if len(word) == length]
    return {key:value}

# families = {"___":[ben] }

def generateFamilies(families, length, guess):
    newFamilies = {}
    for family in families.items():
        for word in family[1]:
            if guess in word:
                temp = ''
                for i in range(length): # instead of .find(), we want to replace all instances of the guess in the chosen word
                    if word[i] == guess:
                        temp += guess
                    else: 
                        temp += '_'
                try:    
                    newFamilies[temp].append(word)
                except: 
                    newFamilies[temp] = [word]
            else:
                try:    
                    newFamilies[family[0]].append(word)
                except: 
                    newFamilies[family[0]] = [word]
    return newFamilies

# pick next family based on number of words left (w/ or w/o guesses)

def pickFamily(families):
    maximum = 0
    maxFam = ""
    for family in families.items():
        if len(family[1]) > maximum:
            maximum = len(family[1])
            maxFam = family[0]
    return {maxFam:families[maxFam]}
        
    
# user guesses letter

def userGuess(guesses):
    guess = ''
    while type(guess) is not str and len(guess) != 1:
        try:
            slowPrint('Please enter a letter you have not guessed yet.', 0.01, "")
            guess = str(input(''))
        except:
            continue
    return [guess, guesses-1]           
        

# print game status "_ _ _ _"
        # takes gameStatus = ['_ _ _ _', ['head', 'body','left arm']]

def printGameStatus(gameStatus, guesses):
    slowPrint(f'Current Progress:{gameStatus[0]}\nYou have {guesses} guesses left.{gameStatus[1]}')
    return gameStatus



def main():
    tutorial()
    difficulty = userDifficulty(cheatword)
    userGuesses = getGuesses(difficulty)
    wordLength = userSetLength()
    families = initFamily(wordLength)
    if difficulty == "impossible":
        while userGuesses > 0:
            guessAndGuesses = userGuess(userGuesses)
            guess = guessAndGuesses[0]
            userGuesses = guessAndGuesses[1]
            families = generateFamilies(families, wordLength, guess)
            newFam = pickFamily(families)
        else:
            """end game"""
    else:
        """Normal hangman woohoo"""

if __name__ == "__main__":
    main()
