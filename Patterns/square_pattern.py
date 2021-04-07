num = int(input("Please enter the number of rows: "))

for rows in range(1 , num + 1):
    for columns in range(1 , num + 1):
        if columns <= rows:
            print(rows , end=" ")
        else:
            print(columns , end=" ")
    print()            
