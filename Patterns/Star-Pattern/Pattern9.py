## Pattern - 9
'''
Example

Input

Input rows: 5
Output

*
**
* *
*  *
*****
'''

num = int(input("Please enter the number of rows: "))

for rows in range(0 , num):
    for columns in range(0 , rows + 1):
        if(rows == 0 or rows == num-1 or columns == 0 or columns == (rows)):
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()            
