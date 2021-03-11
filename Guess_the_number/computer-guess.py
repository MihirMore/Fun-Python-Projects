# Computer guess is a game where computer guesses a secret-number and user says if that number is too low or high or correct.

import random

def computer_guess(x):
    low = 1
    high = x
    response = ""
    while response != "c":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low # b/c high == low 
        response = input(f"is {guess} too high (H), too low(L), or correct(C) guess??: ").lower()
        if response == "h":
                high = guess - 1
        elif response == "l":
                low = guess + 1

    print(f"Yaay! The computer guessed your secret number {guess} correctly.")

limit = int(input("Please enter the limit for guessing. Ex: 1000: "))                               
computer_guess(limit)