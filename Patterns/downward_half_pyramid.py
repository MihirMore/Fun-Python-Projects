rows = int(input("Please enter the number of rows: "))

for row in range(rows + 1, 0 , -1):
    for columns in range(0 , row - 1):
        print("*",end="")
    print()    

