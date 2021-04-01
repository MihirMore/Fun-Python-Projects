while True:
    try:
        name = str(input("Please enter your name: "))
    except:
        print("Please enter a valid name")
        continue
    try:
        dob =  str(input("Please enter your date of birth: "))
    except:
        print("Please enter a valid date")
        continue
    break

print(f"- Name: {name} \n- Date of birth: {dob} \n ")                   