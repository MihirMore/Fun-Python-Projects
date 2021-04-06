n = int(input("Please enter the number of rows: "))

for rows in range(n , 0 , -1):
    for spaces in range(0 , n - rows):
        print(end=" ")
    for columns in range(0 ,rows):
        print("*",end=" ")
    print()  

for rows in range(0 , n):
    for spaces in range(0 , n - rows - 1):
        print(end=" ") 
    for columns in range(0 , rows + 1):
        print("*",end=" ")
    print()
