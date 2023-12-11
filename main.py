import random
from .hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])