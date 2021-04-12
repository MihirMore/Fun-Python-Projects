## Pattern 24
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
    for j in range(0 , 2*i):
        print(" ", end="")
    for k in range(rows-i, 0 , -1):
        print("*" , end="")
    print()
for m in range(1, rows):    
    for n in range((rows*2)-2*m-2,0 , -1):
        print(" ", end="")
    for o in range(0,m+1):
        print("*", end="")                          
    print()
