print(" The character pattern")
asciivalue = 65

for i in range(0 , 5):
    for j in range(0 , i+1):
        alphabet = chr(asciivalue)
        print(alphabet, end=" ")
        asciivalue += 1
    print()



