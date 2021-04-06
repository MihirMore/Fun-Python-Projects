n = int(input("Please enter the number of rows: "))
k = (2 * n) - 2
# Printing simple pyramid first
for rows in range(0 , n):
    for spaces in range(0 , k):
        print(end=" ")
    k -= 1
    for columns in range(0 , rows + 1):
        print("*",end=" ")
    print()
# Printing downward triangle
k = n - 2

for rows in range(n , -1 , -1):
    for spaces in range(k , 0 , -1):
        print(end=" ")
    k += 1
    for columns in range(0 , rows + 1):
        print("* ",end="")
    print()        
