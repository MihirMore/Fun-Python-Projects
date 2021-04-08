## Pattern - 1
'''
Example

Input

Input rows: 5
Input columns: 5
Output

11111
11111
11111
11111
11111
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(0 ,rows):
    for j in range(columns):
        print("1", end=" ")
    print()   


