import random
from words import words
from hangman_visual import lives_visual_dict
import string 

def get_valid_word(words)
    word = random.choice(words)
    while "-" in words or " " in words:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7 

    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives, "lives left and you have used these letters: "," ".join(used_letters))
        

