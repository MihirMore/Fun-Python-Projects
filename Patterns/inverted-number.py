num = int(input("Please enter the number of rows: "))
k = 0
for rows in range( num , 0 , -1):
    k += 1
    for columns in range(1, rows + 1):
        print(k,end=" ")
    print()    