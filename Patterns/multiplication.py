num = int(input("Please enter the number of rows: "))

for rows in range(1 , num + 1):
    for columns in range(1 , rows + 1):
        print(rows * columns, end=" ")
    print() 
   