n = int(input("Enter the number of rows to print: "))

for i in range(0 , n):
    for j in range(0 , i+1):
        print("*",end="")
    print()    
