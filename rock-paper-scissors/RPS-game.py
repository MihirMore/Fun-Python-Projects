import random   

def play():
    user = input("What's your choice? Rock 'r', Paper 'p', Scissors 's': ").lower()
    computer = random.choice(['r', 'p' , 's'])

    print(f"Computer chose {computer}")

    if user == computer:
        return "It's a tie!"

    if who_wins ( user, computer ):
        return "You won!"

    return "You lost!"

def who_wins( player , opponent):

    if( player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r'):
        return True

print(play())