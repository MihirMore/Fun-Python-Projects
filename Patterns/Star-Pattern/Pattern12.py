## Pattern - 12
'''
Example

Input

Input rows: 5
Output

    *
   **
  * *
 *  *
*****
'''

num = int(input("Please enter the number of rows: "))

for i in range(0 , num):
    for j in range(num-i-1 , -1 , -1):
        print(" ", end=" ")
    for k in range(0 , i+1):
        if( i == 0 or i == num-1 or k == 0 or k == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()