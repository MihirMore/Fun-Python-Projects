n = int(input("Please enter the number of rows: "))

m = (2 * n) - 2
for rows in range(n , -1 , -1):
    for spaces in range(m , 0 , -1):
        print(end=" ")
    m += 1
    for columns in range(0 , rows + 1):
        print("*",end=" ")
    print()




