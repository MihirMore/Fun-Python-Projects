## Pattern - 18
'''
Example

Input

Input rows: 5
Output

*********
 *******
  *****
   ***
    *
'''
rows = int(input("Please enter the number of rows: "))

for i in range(0 , rows):
    for j in range(0 , i):
        print(" ", end=" ")
    for k in range((rows*2)-(2*i+1) , 0 , -1):
        print("*" , end=" ")
    print()          