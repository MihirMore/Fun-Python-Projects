def armstrongcheck(testednumber):
    result = 0
    while (testednumber != 0):    
        remainder = testednumber % 10
        result += remainder ** 3          
        testednumber = int(testednumber/10)         
    return result

def main():
    print("\n Armstrong number checker")
    originalnumber = int(input("\n Please enter an integer to check if it's an Armstrong number: "))
    checkedNumber = armstrongcheck(originalnumber)
    if checkedNumber == originalnumber:
        print("It's an Armstrong number!")
    else:
        print("It's not an Armstrong number")

main()
    


  