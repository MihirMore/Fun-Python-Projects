email = input("Please enter your email id: ").strip()

user_name = email[:email.index("@")]

domain_name = email[email.index("@")+1:]

output = f"Your username is {user_name} and your domain name is {domain_name}"

print(output)

