## Pattern -1 
'''
Example

Input

Input number of rows: 5
Output

*****
*****
*****
*****
*****
'''
num = int(input("Please enter number of rows: "))

for rows in range(0 , num):
    for columns in range(0 , num):
        print("*" , end=" ")
    print()    