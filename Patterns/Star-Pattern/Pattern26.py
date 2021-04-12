## Pattern - 26
'''
Example

Input

Input N: 5
Output

    +
    +
    +
    +
+++++++++
    +
    +
    +
    +
'''
rows = int(input("Please enter the number of rows: "))

for i in range(0 , rows*2):
    if(i<rows-1):
        for j in range(0 , rows-1):
            print(" ",end=" ")
        print("+", end=" ")
        print()    
    elif (i == rows-1):
        for k in range(0 ,(rows*2)-1):
            print("+",end=" ")
        print()
    elif (i > rows):
        for m in range(0 , rows-1):
            print(" ",end=" ")
        print("+", end=" ")
        print()



