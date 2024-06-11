#   Task 1: Input Length Validator


first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')

if len(first_name) < 2 or len(last_name) < 2:
    print("Names must be at least 2 characters long, please try again ")

else:
    print()
    print("First:", len(first_name))
    print("Last", len(last_name))