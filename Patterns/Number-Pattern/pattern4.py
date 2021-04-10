## Pattern - 4
'''
Example

Input

Input rows: 5
Input columns: 5
Output

11111
10001
10001
10001
11111
'''

rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(0 , rows):
    for j in range(0 , columns):
        if (i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print("1" , end=" ")
        else:
            print("0" , end=" ")
    print()        
