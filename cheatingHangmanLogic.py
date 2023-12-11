# basic logic for cheating hangman written in python
# we dont want to write the whole game in here, this is just experimental
# kind of like a brainstorming page. any features we want to add should start
# in this file
from time import sleep
import random
gameWordList = open("words_alpha.csv", 'r').read().split('\n')
# utlitiy print function

def slowPrint(string, delay = .1, end="\n"):
    """given a string, print each character with given delay, and given an end character"""
    for char in string:
        print(char, end='', flush=True)
        sleep(delay)
    print(end)

# tutorial

def tutorial():
    slowPrint("Welcome to Hangman Unmastered!", 0.15)
    slowPrint("If you do not know how to play, enter \'Teach me.\' If you do, enter nothing.", 0.01)
    tutorial = str(input("Enter:"))
    while tutorial.lower() == "teach me":
        slowPrint(
            """These are the rules. At the start of each game, I will pick a word. Don't worry, I'll go easy if you ask nicely.\nEach turn, you get a chance to guess a letter. If the letter you guessed is in the word, I'll tell you. If it isn't,\nI'll tell you. I promise to tell the truth :D.""", 0.01
        )
        slowPrint('Do you understand the rules? If not, enter \'Teach me\'.', 0.01)
        tutorial = str(input("Enter:"))

# validates if guess number is valid

def validGuess(difficulty, guesses, maxG = 25):
    if type(guesses) != int:
        return [False]
    elif difficulty == "hard":
        maxG = 6
    elif difficulty == "easy" or difficulty == "impossible":
        maxG = 25
    if guesses > maxG or guesses <= 0:
        return [False]
    return [True, maxG]

# user declares guess amount

def getGuesses(difficulty):
    if difficulty == "easy" or difficulty == "impossible":
        slowPrint("How many guesses would you like? The maximum is 25.", 0.01)
    elif difficulty == "hard":
        slowPrint("Due to your difficulty choice, you only get 6 or less guesses. Please choose how many guesses you would like.", 0.01)
    while True:
        try:
            guesses = int(input("Guesses:"))
            validity = validGuess(difficulty, guesses)
            if validity[0]:
                slowPrint(f"Alright, {guesses} guesses it is!", 0.01)
                return guesses
            else:
                if difficulty == "hard":
                    slowPrint("That is an invalid amount of guesses. Please enter a number between 1 and 6.", 0.01)
                else:
                    slowPrint("That is an invalid amount of guesses. Please enter a number between 1 and 25.", 0.01)
        except ValueError:
            slowPrint("Please enter a valid number.", 0.01)

# user decide difficulty

def userDifficulty():
    """Allows a user to choose from Easy, Hard and Impossible"""
    possDiff = ['easy','hard','impossible']
    slowPrint("What difficulty would you like? Choose from Easy, Hard, and Impossible.", 0.01)
    difficulty = input("Difficulty:").lower()
    while difficulty not in possDiff:
        slowPrint("Please try again. You may have made a typo.", 0.01)
        difficulty = input("Difficulty:").lower()
    if difficulty in possDiff:
        slowPrint(f"You have chosen {difficulty}, good luck!", 0.01)
        if difficulty == "impossible":
            slowPrint("You have made a big mistake. Mwahahaha!", 0.01)
    return difficulty

# user set length

def userSetLength():
    length = -1
    while type(length) is not int or (length > 8 or length < 2):
        try: 
            slowPrint("How long can my word be?\nEnter a number between 2 and 8:", 0.01)
            length = int(input("Enter:"))
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

def userGuess():
    guess = ''
    while type(guess) is not str or len(guess) != 1:
        try:
            slowPrint('Please enter a letter you have not guessed yet.', 0.01, "")
            guess = str(input(''))
        except:
            continue
    return guess          
        

# print game status "_ _ _ _"
        # takes gameStatus = '_ _ _ _']

def printGameStatus(families, guesses):
    status = list(families.keys())[0]
    slowPrint(f'Current Progress:{status}\nYou have {guesses} guesses left.', 0.01)
    
# hangman for easy and hard difficulties
def hangman(gameWordList, wordLength, guesses):
    chosen_word = random.choice(gameWordList)
    wordLength = len(chosen_word)
    end_of_game = False
    display = []
    for _ in range(wordLength):
        display += "_"
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(wordLength):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            guesses -= 1
            if guesses == 0:
                end_of_game = True
                print("You lose.")

###
# game start
# user chooses length
# initialize families
# user guesses
# generate new families
# pick new family
# check if user wins
# loop                  ### 

def main():
    incorrectGuesses = 0
    letterGuesses = []
    tutorial()
    difficulty = userDifficulty()
    userGuesses = getGuesses(difficulty)
    wordLength = userSetLength()
    families = initFamily(wordLength)
    if difficulty == "impossible":
        while userGuesses > 0:
            guess = userGuess()
            while guess in letterGuesses:
                slowPrint("You have already guessed this letter, try again.", 0.01)
                guess = userGuess()
            families = generateFamilies(families, wordLength, guess)
            families = pickFamily(families)
            userGuesses -= 1
            printGameStatus(families, userGuesses)
            letterGuesses+= guess
            slowPrint(f"You have guessed {letterGuesses} so far.", 0.01)
            if "_" not in list(families.keys())[0]:
                slowPrint("What... what is happening? How did you guess that?\nYou've... beaten me... impossible. Well done.\nYOU WIN!")
        else:
            slowPrint(f'Nice try, but you lost. Good game!\nThe word was {random.choice(list(families.keys())[0])}.')
    elif difficulty:
        """Normal hangman woohoo"""
        hangman(gameWordList, wordLength, userGuesses)
if __name__ == "__main__":
    main()
