print("WELCOME TO SUPER MEGA SERVICE!!!")

name = input("Enter your name: ")
email = input("Enter your email address: ")
password = input("Your password is: ")


if name == "Derek" or name == "Suzan":
    print("Your name is", name)
    print("Your password is secret")
    button = input("For service email press F: ")

    if button == "F":
        print("RESPECT")
        print("Message was send to your address")
    else:
        print("INVALID BUTTON")
        print("TERMINATED")
else:
    print("WHO R U?")
