## Pattern - 16
'''
Example

Input

Input rows: 5
Output

    *
   ***
  *****
 *******
*********
'''
rows = int(input("Please enter the number of rows: "))

for i in range(0 , rows):
    for j in range(rows-i-1 , -1 , -1):
        print(" ", end=" ")
    for k in range(0 , 2*i+1):
        print("*" , end=" ")
    print()          

