## Pattern - 14
'''
Example

Input

Input rows: 5
Input columns: 5
Output

55555
54444
54333
54322
54321
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(rows , 0 , -1):
    k = i
    for j in range(0 , columns):
        if(k == 5):
            print("5", end=" ")
        else:
            print(k , end=" ")
            k += 1    
    print()