number = int(input("Please enter the number of rows: "))

for rows in range( number , 0 , -1):
    for columns in range(0 , rows):
        print(number , end=" ")
    print()    