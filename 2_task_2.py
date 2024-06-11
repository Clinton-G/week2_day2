#   Task 2: Password Complexity Checker

def password_requirement(password):
    if len(password) < 8:
        print('Must Contain 8 Chars')

    elif not any(up.isupper() for up in password):
        print('Must Contain an Uppercase Letter')

    elif not any(low.islower() for low in password):
        print('Must Contain a Lowercase Letter')

    elif not any(char.isdigit() for char in password):
        print('Must Contain a Number')

    else:
        print("Password Accepted")

print('Password Must Contain 8 Chars, One Uppercase, One Lowercase, & One Number')
password = input("Enter your password: ")
password_requirement(password)