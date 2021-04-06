number = int(input("Please enter the number of rows: "))

for rows in range( number + 1):
    for columns in range(rows):
        print(rows,end=" ")
    print()    