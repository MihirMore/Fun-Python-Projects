while True:
    try:
        user_input = int(input("Please enter a integer between 0 to 1000: "))
    except:
        print("Please enter a numeric value")
        continue   
    if user_input < 1:
        print("Please enter a positive integer")
        continue
    break    

if (user_input % 2) == 0:
    print("That's an even number!")
else:
    print("That's odd number!")       