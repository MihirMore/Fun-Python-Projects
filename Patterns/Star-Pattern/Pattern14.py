## Pattern - 15
'''
Example

Input

Input rows: 5
Output

*****
*  *
* *
**
*
'''

num = int(input("Please enter the number of rows: "))

for i in range(0 , num):
    for j in range(num-i , 0 , -1):
        if(i == 0 or i == num-1 or j == 1 or j == num-i):
            print("*" , end=" ")
        else:
            print(" ", end=" ")
    print()            