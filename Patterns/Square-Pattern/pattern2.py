## Pattern - 2
'''
Example

Input

Input rows: 5
Input columns: 5
Output

11111
00000
11111
00000
11111
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(0 , rows):
    for j in range(0 , columns):
        if (i % 2) == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()            