n = int(input("Please enter the number of rows: "))

for rows in range( n + 1, 0, -1):
    for columns in range(0 , n):
        print("*",end="")
    n = n - 1    
    print()    