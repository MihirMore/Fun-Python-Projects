print("The character pattern")
number = int(input("Please enter a Ascii value between 65-122: "))

if (number >= 65 and number <= 122):
    for rows in range(0 , 5):
        for columns in range(0 , rows + 1):
            alphabet = chr(number)
            print(alphabet , end=" ")
        print()    
else:
    print("Enter a valid ascii value")

