## Pattern - 29
'''
Example

Input

Input N: 10
Output

  *****     *****
 *******   *******
********* *********
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
'''
rows = int(input("Please enter the number of rows: "))
count = int(rows/2)
total = rows*2
for i in range(count , rows+1,2):
    for j in range(1, rows-i,2):
        print(" ",end="")        
    for k in range(1, i+1):
        print("*",end="")         
    for l in range(0, rows-i):
        print(" ", end="")          
    for m in range(1, i+1):
        print("*",end="")          
    print()
for row in range(rows, 0 ,-1):
    for columns in range(row,rows):
        print(" ", end="")
    for n in range(0 ,(row*2)-1):
        print("*", end="")
    print()          




