#Validating User Input practice
# 1. Username must not be more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits
username = input("Please enter your username: ")
if len(username) > 12:
    print("Your username must not be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Your username must not contain spaces")
elif not username.isalpha():
    print("Your username must not contain digits")
else:
    print("Welcome " + username)

