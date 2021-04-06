number = int(input("Please enter the number of rows: "))

for rows in range( 1 , number + 1):
    for columns in range( 1 , rows + 1):
        print(columns, end=" ")
    print()    