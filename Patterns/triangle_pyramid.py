n = int(input("Please enter the number of rows: "))

m = (n * 2) - 2
for rows in range(0 , n):
    for spaces in range(0 , m):
        print(end=" ")
    m -= 1
    for columns in range (0 , rows + 1):
        print("* ",end="")
    print()