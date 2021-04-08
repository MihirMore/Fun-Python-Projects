## Pattern - 17
'''
Example

Input

Input N: 5
Output

12345
21234
32123
43212
54321
'''
n = int(input("Please enter number of rows: "))
for i in range(1 , n+1):    
    for j in range(i , 1 , -1):
        print(j , end=" ")
    for k in range(1 , n + 2 - i):
        print(k , end=" ")                      
    print()

