## Pattern - 3
'''
Example

Input

Input rows: 5
Input columns: 5
Output

01010
01010
01010
01010
01010
'''

rows = int(input("Please enter the numbe of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(0 , rows):
    for j in range(0 , columns):
        if (j % 2) == 0:
            print("0" , end=" ")
        else:
            print("1" , end=" ")   
    print()         

