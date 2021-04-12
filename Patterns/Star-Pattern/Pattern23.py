## Pattern - 23
'''
Example

Input

Input N: 5
Output

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

rows = int(input("Please enter the number of rows: "))

for i in range(0 , rows):
    for j in range(rows , i , -1):
        print("*" , end=" ")
    for spaces in range(0, 2*i):
        print(" ", end=" ")
    for k in range(rows ,i , -1):
        print("*" , end=" ") 
    print()
for m in range(0, rows):
    for n in range(0 , m+1):
        print("*" , end=" ")
    for space in range((2*rows-2) , 2*m, -1):
        print(" ", end=" ")
    for c in range(0 , m+1):
        print("*" , end=" ")
    print()           


