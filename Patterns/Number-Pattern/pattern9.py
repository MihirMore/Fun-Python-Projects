## Pattern - 9
'''
Example

Input

Input rows: 5
Input cols: 5
Output

01110
10001
10001
10001
01110
'''

rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(0 , rows):
    for j in range(0 , columns):
        if( (i == 0 or i == rows - 1) and (j == 0 or j == columns - 1)):
            print("0" , end=" ")
        elif((j == 0 or j == (columns - 1)) or (i == 0 or i == (rows - 1))):
            print("1" , end=" ")
        else:
            print("0" , end=" ")    
    print()
