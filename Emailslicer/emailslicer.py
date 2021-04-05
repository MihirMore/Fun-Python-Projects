email = input("Please enter your email id: ").strip()

user_name = email[:email.index("@")]

print(user_name)