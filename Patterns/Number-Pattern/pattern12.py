## Pattern - 12
'''
Example

Input

Input rows: 5
Input columns: 5
Output

12345
23456
34567
45678
56789
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))
k = 1
for i in range(0 , rows):
    k += i
    for j in range(0 , columns):
        print(k , end=" ")
        k += 1
    print() 
    k = 1   