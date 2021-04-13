## Pattern - 28
'''
Example

Input

Input N: 5
Output

 ***
*   *
*   *
*   *
 ***
*   *
*   *
*   *
 ***
'''

rows = int(input("Please enter the number of rows: "))
count = (rows*2)-1
for i in range(0 , count):
    for j in range(0 , rows):
        if ((i == 0 and (j == 0 or j == rows-1)) or (i == rows-1 and (j == 0 or j == rows-1)) or (i == count-1 and (j == 0 or j == rows-1))):
            print(" ", end="")
        elif (i == 0 or i == rows-1 or i == count-1 or j == 0 or j == rows-1):
            print("*" , end="")
        else:
            print(" ",end="")
    print()                  