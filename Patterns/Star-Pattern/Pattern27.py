## Pattern -27
'''
Example

Input

Input N: 5
Output

*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
'''
rows = int(input("Please enter the number of rows: "))
count = (rows*2)-1
for i in range(0, count):
    for j in range(0 , count):
        if (i == j or j == count - i-1):
            print("*" , end="")
        else:
            print(" ", end="")
    print()      

