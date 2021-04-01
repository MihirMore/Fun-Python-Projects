while True:
    try:
        tip = float(input("Please enter your bill amount:$"))
    except:
        print("Please enter a valid number")
        continue
    break
eightip = tip * 0.18
twentytip = tip * .20
twentyfivetip = tip * .25
amount = int(input("What amount of tip would you like to give: 18%, 20%, 25% (Enter only number): "))
if(amount == 18):
    total1 = tip + eightip
    print(f"18% tip is ${eightip}, which brings your total to {total1}")
elif(amount == 20):
    total2 = tip + twentytip
    print(f"20% tip is ${twentytip}, which brings your total to {total2}")
elif(amount == 25):
    total3 = tip + twentyfivetip
    print(f"25% tip is ${twentyfivetip}, which brings your total to {total3}")        
