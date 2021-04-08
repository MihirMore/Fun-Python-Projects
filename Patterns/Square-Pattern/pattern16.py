## Pattern - 16
'''
Example

Input

Input rows: 5
Input columns: 5
Output

12345
23451
34521
45321
54321
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(1 , rows+1):
    k = i
    for j in range(0 , columns):
        if(k <= 5):
            print(k , end=" ")
            k += 1
        else:
            print((((columns+1) - j)-1), end=" ")

    print()        
