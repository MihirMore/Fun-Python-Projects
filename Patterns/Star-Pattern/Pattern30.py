## Pattern - 30
'''
Example

Input

Input N: 10
Output

  *****     *****  
 *******   ******* 
********* *********
*****mihirmore*****
 ***************** 
  ***************  
   *************   
    ***********    
     *********     
      *******      
       *****       
        ***        
         *
'''
rows = int(input("Please enter the number of rows: "))
name = input("Please enter the name to print: ").lower()
nam_len = len(name)
count = int(rows/2)
mid = int(((rows*2)-nam_len)/2)
for i in range(count , rows+1,2):
    for j in range(1, rows-i,2):
        print(" ",end="")        
    for k in range(1, i+1):
        print("*",end="")         
    for l in range(0, rows-i):
        print(" ", end="")          
    for m in range(1, i+1):
        print("*",end="")          
    print()
for row in range(rows, 0 ,-1):
    for columns in range(row, rows):
        print(" ",end="")
    # Print the string
    if(row == rows):
        for n in range(1, mid+1):
            print("*", end="")
        print(name,end="")
        for r in range(1, mid+1):
            print("*", end="")
    else:
        for s in range(0 ,(row*2)-1):
            print("*", end="")
    print()      


