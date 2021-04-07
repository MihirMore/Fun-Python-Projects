num = int(input("Please enter the number of rows: "))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(i*2 -1, end=" ")
        j = j + 1
    i = i + 1
    print()    