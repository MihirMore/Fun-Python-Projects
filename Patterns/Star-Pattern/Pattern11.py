## Pattern - 11
'''
Example

Input

Input rows: 5
Output

*****
 ****
  ***
   **
    *
'''
num = int(input("Please enter the number of rows: "))

for i in range(0 , num):
    for j in range(0 , i):
        print(" ", end=" ")
    for k in range(num-i , 0 , -1):     
        print("*" , end=" ")
    print()     

