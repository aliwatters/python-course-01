
password = ""
while (password != "secret"):
    password = input("Enter your password: ")
    if password == "secret":
        print("You are logged in")
    else:
        print("Sorry try again")
