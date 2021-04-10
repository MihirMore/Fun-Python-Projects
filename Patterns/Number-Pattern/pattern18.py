MAX = 100
  
# function to Print pattern 
def prints(a, size): 
    for i in range(size): 
        for j in range(size):
            print(a[i][j], end = '')
        print()


def innerPattern(n): 
      
    # Pattern Size 
    size = 2 * n - 1
    front = 0
    back = size - 1
    a = [[0 for i in range(MAX)]  
            for i in range(MAX)]
    while (n != 0): 
        for i in range(front, back + 1):
            for j in range(front, back + 1):
                if (i == front or i == back or
                    j == front or j == back):
                    a[i][j] = n
        front += 1
        back -= 1
        n -= 1
    prints(a, size)        

n = int(input("Please enter the number of rows: "))
  
# function calling 
innerPattern(n)    