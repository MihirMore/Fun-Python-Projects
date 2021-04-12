## Pattern - 25 
'''
Example

Input

Input N: 5
Output

    *****
   ****
  ***
 **
*
 **
  ***
   ****
    *****
'''
rows = int(input("Please enter the number of rows: "))

for i in range(0 , rows):
    for j in range(rows-i-1, 0, -1):
        print(" " , end="")
    for k in range(rows-i, 0, -1):
        print("*", end="")
    print()  
for m in range(0,rows-1):
    for c in range(1, m+2):
        print(" ", end="")  
    for n in range(0, m+2):
        print("*", end="")       
    print()     



