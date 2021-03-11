# Guess the number is a game where user is asked to guess a number, the computer then comments if the number is high, low or the correct number.
# Here  we are using the random function to generate a random number betwwen x to y.
  
import random

def guess(x):
            random_number = random.randint(1, x)
            guess = 0
            while guess != random_number:
                guess = int(input(f"Guess a integer between 1 and {x}: "))
                if guess < random_number:
                    print("Oops!, guess again. You guessed too low.")
                elif guess > random_number:
                    print("Oops!, guess again. You guessed too high.")

            print(f"Yay! Congrats you've guessed the number {random_number}.")

guess(10)                   


