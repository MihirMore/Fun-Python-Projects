print("Print equilateral triangle Pyramid with characters")
num = int(input("Please enter the number of rows: "))

asciiValue = 65
for rows in range(0 , num):
    for spaces in range(0 , num - rows - 1):
        print(end=" ")
    for columns in range(0 , rows + 1):
            alphabet = chr(asciiValue)
            asciiValue += 1
            print(alphabet, end=" ")
    print()    