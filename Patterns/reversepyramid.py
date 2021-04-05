n = int(input("Please enter the number of rows: "))

k = n - 1

for rows in range(0 , n):
    for spaces in range(0 , k):
        print(end=" ")
    k = k - 1
    for columns in range(0 , rows + 1):
        print("* ",end="")
    print()        
