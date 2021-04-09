## Pattern - 3
'''
Example
Input
Enter number of rows: 5
Output

*****
** **
* * *
** **
*****
'''

num = int(input("Please enter the number of rows: "))

for rows in range(1 , num+1):
    for columns in range(1 , num+1):
        if(rows == 1 or rows == num or columns == 1 or columns == num  or rows == columns or columns == (num - rows + 1)):
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()            