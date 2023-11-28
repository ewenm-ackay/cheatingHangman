# basic logic for cheating hangman written in python
# we dont want to write the whole game in here, this is just experimental
# kind of like a brainstorming page. any features we want to add should start
# in this file

from time import sleep

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

userStart()


# print game status "_ _ _ _"

def gameStatus():
    pass
# take user guess



# generate new families {"_ _ _ _": listOfWords}




