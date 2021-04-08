## Pattern - 6
'''
Example

Input

Input rows: 5
Input columns: 5
Output

10101
01010
10101
01010
10101
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

k = 1

for i in range(0 , rows):
    for j in range(0 , columns):
        if( k == 1):
            print("1" , end=" ")
        else:
            print("0" , end=" ")

        k *= -1
    if(columns % 2) == 0:
        k *= -1
    print()                

