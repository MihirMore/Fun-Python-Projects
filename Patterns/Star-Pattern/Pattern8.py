## Pattern - 8
'''
Example

Input

Input number of rows: 5
Output

*
**
***
****
*****
'''
num = int(input("Please enter the number of rows: "))

for rows in range(0 , num):
    for columns in range(0 , rows+1):
         print("*" , end="")
    print()