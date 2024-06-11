#   Task 1: Command Parser

def text_input(text):
    prompt = {
        "help": "Happy To Help. ",
        "contact support": "Call 012-345-6789, to speak with support "
    }

    for user_input in prompt:
        if user_input in text:
            return prompt[user_input]

    if "issue" in text:
        issue_help = input('''What Issues Are You Experiencing?
        
        1: Login Issues
        2: Performance Issues
        3: Error Codes
        
        Enter Choice: ''')
        if issue_help == '1':
            return '\n What Login Issues Are You Experiencing?'
        elif issue_help == '2':
            return "\n What Performance Issues Are You Experiencing?"
        elif issue_help == '3':
            return '\n What Error Codes Are You Receiving?'
        else:
            return 'Invalid Input, Try Again'


    return 'Invalid Input, Try Again'


user_input = input("Enter Prompt: ")
print(text_input(user_input))
