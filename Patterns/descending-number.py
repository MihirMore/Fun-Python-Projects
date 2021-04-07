number = int(input("Please enter the number of rows: "))

for rows in range(0 , number + 1):
    for columns in range(number - rows , 0 , -1):
        print(columns , end=" ")
    print()
