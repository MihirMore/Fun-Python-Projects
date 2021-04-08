## Pattern - 16
'''
Example

Input

Input rows: 5
Input columns: 5
Output

12345 55555
23455 45555  
34555 34555
45555 23455
55555 12345
'''
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(1 , rows+1): 
    k = i
    for j in range(0 , columns):
        if( k >= 5):
            print("5" , end=" ")
        else:
            print(k , end=" ")
            k += 1          
    
    print()    
