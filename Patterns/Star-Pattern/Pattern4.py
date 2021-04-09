## Pattern - 4
'''
Example

Input

Enter number of rows: 5
Output

    *****
   *****
  *****
 *****
*****
'''
num = int(input("Please enter the number of rows: "))

for rows in range(0 , num):
    for spaces in range(num-rows-1 , -1 , -1):
        print(" " , end="")
    for columns in range(0 , num):
        print("*" , end=" ")
    print()        


