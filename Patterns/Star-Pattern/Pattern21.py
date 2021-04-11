## Pattern - 21
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
 ****
  ***
   **
    *
'''
rows = int(input("Please enter the number of rows: "))
space = rows-2
star = 1
for i in range(0 , rows*2):
    for spaces in range(space , -1, -1):
        print(" ", end=" ")        
    for stars in range(0 ,star):
        print("*" , end=" ")        
    if (i < rows-1):
        star += 1
        space -= 1
    else:
        star -= 1
        space += 1      
    print()                                 