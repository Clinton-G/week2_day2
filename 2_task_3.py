#   Task 3: Email Formatter
import re

def email_format(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email):
        return email

    else:
        print('Email must be in Standard Format: exampl@example.com')


email = input("Enter Email: ")
print()
print(email_format(email), "is valid")