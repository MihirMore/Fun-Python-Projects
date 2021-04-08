## Pattern - 7 
'''
Example

Input

Input rows: 5
Input columns: 5
Output

11011
11011
00000
11011
11011
'''

rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

midrows = (rows + 1) / 2
midcolumns = (columns + 1) / 2

for i in range(0 , rows):
    for j in range(0 , columns):
        if( (i == midrows - 1) or (j == midcolumns - 1) ):
            print("0" , end="")
        elif( j == 2 ):
            print("0" , end="")
        else:
            print("1" , end="")    
    print()        
