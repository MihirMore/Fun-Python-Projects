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
    try:
        address = str(input("Please enter you address: "))
    except:
        print("Please enter a valid address")
        continue
    try:
        personal_goals = str(input("What is your career goal?: "))
    except:
        print("Please enter a valid string")
        continue                
    break

print(f"- Name: {name} \n- Date of birth: {dob} \n- Address: {address}\n- Personal Goals: {personal_goals} ")                   