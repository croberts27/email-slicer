# get user email address
email = input("What is your email address?: ").strip()
# slice out user name
user_name = email[:email.index("@")]
# slice out domain name
domain = email[email.index("@") + 1:]
# format message
message = "Your username is {} and your domain name is {}"
output = message.format(user_name, domain)
# display output message
print(output)