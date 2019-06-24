'''
yet another attempt at building calculator
'''
# Basic Import statements:
## import math
# Basic Definations
# Defining error class
class InvalidOperator (Exception):
    def __init__(self, symbol):
        self.wrong_operator = symbol
        self.message = ("The Operator", self.wrong_operator, "is not coded in yet.")
# Taking user input
user_input = input("Enter the expression: ")
# Checking user input for correct operators and,:
# Checking user input (ex - 2+3 is valid but 2++3 is invalid) 
expression = list(user_input)
operators_details = [['+', 2, 'left'],['-', 2, 'left'],['*', 3, 'left'],['/', 3, 'left']]
allowed_operators = [n[0] for n in operators_details]
expression_validity = None
operator_allowed = True
for item in expression:
    try:
        int_item = int(item)
    except ValueError:
        if operator_allowed == True:
            if item not in allowed_operators:
                expression_validity = False
                '''
                Commented lines are for debugging only.
                '''
                print ('operator', item, 'invalid. terminating now...')
                exit()
            else:
                # print ('operator', item, 'found')
                operator_allowed = False
                expression_validity = True
        else:
            print ("Cannot insert an operator after an operator. terminating now...")
            exit()
    else:
        # print ("digit", item, 'found')
        operator_allowed = True
print ("Test Passed. Expression is Valid")
# Initial Conditions
previous_number = 0
token_stack = []
# Converting user input to tokens
for current_item in expression:
    try:
        int_current_item = int(current_item)
    except ValueError:
        token_stack.append(previous_number)
        token_stack.append(current_item)
        previous_number = 0
    else:
        previous_number = 10*previous_number + int_current_item
token_stack.append(previous_number)
print (*token_stack)
# more initial conditions
operator_stack = []
output_stack = []
operator_stack_precedence = 0
# operator precedence parser, too much buggy here.
for token in token_stack:
    try:
        int_token = int(token)
    except ValueError:
        for operators in operators_details:
            n = operators[0]
            n_precedence = operators[1]
            if n ==token:
                if n_precedence > operator_stack_precedence:
                    operator_stack.append(n)
                    operator_stack_precedence = n_precedence
                elif n_precedence == operator_stack_precedence:
                    output_stack.append(operator_stack.pop())
                    operator_stack.append(n)
                else:
                    for _ in range(len(operator_stack)):
                        output_stack.append(operator_stack.pop())
                    operator_stack.append(n)
                    operator_stack_precedence = n_precedence
    else:
        output_stack.append(int_token)
for _ in range(len(operator_stack)):
    output_stack.append(operator_stack.pop())
# Display Final Condition
print ("Final Output Stack looks as follows: \n", *output_stack)
# print ("Final operator stack looks as follows: \n", *operator_stack)
# TODO: do real calculation on parsed output.

