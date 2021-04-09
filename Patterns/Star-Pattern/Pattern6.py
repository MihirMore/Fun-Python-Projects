## Pattern - 6
'''
Example

Input

Input rows: 5
Output

*****
 *****
  *****
   *****
    *****
'''
num = int(input("Please enter the number of rows: "))

for rows in range(0 , num):
    for spaces in range(0 , rows):
        print(" ", end="")
    for columns in range(0 , num):
        print("*" , end=" ") 
    print()       