## Pattern - 20
'''
Example

Input

Input rows: 5
Output

*
**
***
****
*****
****
***
**
*
'''

rows = int(input("Please enter the number of rows: "))
columns = 1
for i in range(0 , rows*2):
    for j in range(1 , columns):
        print("*", end=" ")
    if(i < rows):
        columns += 1
    else:
        columns -= 1         
    print()          