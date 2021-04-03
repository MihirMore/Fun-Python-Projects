def armstrongcheck(testednumber):
    result = 0
    while (testednumber != 0):    
        remainder = testednumber % 10
        result += remainder ** 3          
        testednumber = int(testednumber/10)         
    return result

def main():
            
    


  