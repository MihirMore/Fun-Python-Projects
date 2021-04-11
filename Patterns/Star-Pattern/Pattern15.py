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

rows = int(input("Please enter the number of rows: "))

for i in range(0 , rows):
    for j in range(0 , i):
        print(" ", end=" ")
    for k in range(rows-i , 0 ,-1):
        if(i == rows-1 or i == 0 or k == 1 or k == rows-i):
            print("*" , end=" ")
        else:
            print(" " , end=" ")    
    print()          