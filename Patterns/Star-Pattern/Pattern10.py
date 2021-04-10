## Pattern - 10
'''
Example

Input

Input rows: 5
Output

    *
   **
  ***
 ****
*****
'''

num = int(input("Please enter the number of rows: "))

for i in range(0 , num):
    for j in range(num-i-1 , -1 , -1):
        print(" " , end=" ")
    for k in range(0 , i+1):
        print("*" , end=" ")
    print()    
