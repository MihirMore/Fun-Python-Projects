## Pattern - 5
'''
Example

Input

Input number of rows: 5
Output

    *****
   *   *
  *   *
 *   *
*****
'''
num = int(input("Please enter the number of rows: "))

for rows in range(0 , num):
    for spaces in range(num-rows-1 , -1 , -1):
        print(" ", end="")
    for columns in range(0 , num):
        if(rows == 0 or rows == num-1 or columns == 0 or columns == num -1):
            print("*" , end="")
        else:
            print(" ", end="")

    print()            