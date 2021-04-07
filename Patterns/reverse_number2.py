## Pattern
'''
1
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

'''
num = int(input("Please enter the number of rows: "))

for rows in range(0 , num):
    for columns in range(rows + 1 , 0 , -1):
        print(columns , end=" ")
    print()    
