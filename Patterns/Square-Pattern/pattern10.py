## Pattern - 10
'''
Example

Input

Input rows: 5
Input columns: 5
Output

11111
22222
33333
44444
55555
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(1 , rows + 1):
    for j in range(1 , columns + 1):
        print(i , end=" ")
    print()    