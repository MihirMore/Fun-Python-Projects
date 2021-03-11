# Madlibs is a fun program which accepts user input and creates a story based on the input.
# You can create your own madlib using this template.
# Accept the data from user. This will be used as fillers for our story.

name = input("Please enter a name: ")
sillyWord = input("Please enter a silly word: ")
number = input("Please enter a number: ")
adjective1 = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
adjective2 = input("Please enter an adjective: ")
relative = input("Please enter the name of a relative: ")
adjective3 = input("Please enter an adjective: ")
verb = input("Please enter a verb: ")
adjective4 =  input("Please enter an adjective: ")
adjective5 = input("Please enter an adjective: ")

# Create a story and store it in madlib variable

madlib = (f"Hello my name is astronaut {name}. I'm on my way  \n to planet {sillyWord}. I'll be gone for {number} days. \n I'm very {adjective1} about the trip but I'll miss my {noun}. \n I've heard that the atmosphere there is {adjective2}. Luckily \n my {relative} packed me a jacket to keep me {adjective3}. When I land \n on the planet I'll {verb} for joy. I'm {adjective4} \n to walk on another planet. I could not be more {adjective5} for this trip!")

# Print the madlib

print(madlib)