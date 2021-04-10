## Pattern - 13
'''
Example

Input

Input rows: 5
Input columns: 5
Output

1  2  3  4  5
6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

k = 1

for i in range(0 , rows):
    for j in range(0 , columns):
        print(k , end=" ")
        k += 1
    print()    