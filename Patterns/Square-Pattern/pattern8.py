## Pattern - 8
'''
Example

Input

Input rows: 5
Input columns: 5
Output

10001
01010
00100
01010
10001
'''

rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(0 , rows):
    for j in range(0 , columns):
        if (i == j or j == (columns-1) - i):
            print("1" , end=" ")
        else:
            print("0" , end=" ")
    print()            