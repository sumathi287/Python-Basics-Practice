user_name = input("Enter your user name: ")

if user_name == "admin":
    password = int(input("Enter your password: "))
    if password == 12345:
        print("Login Successfully!!")
    else:
        print("Invalid password!!")
else:
    print("Invalid user name")
