#! /
'''
An attempt at building calculator
Supports only right hand class of notations
Simpe 
'''
# Basic import statements
# Defining Error Classes
class OperatorNotValid(Exception):
    def __init__(self, token):
        self.wrong_operator = token
        self.message = "The Operator", self.wrong_operator, "is not coded in yet."
        print (self.message)
# Taking User Input
inp = input("Enter the expression: ")
# List of allowed operators with its precedence
allowed_operators = [['+', 2],['-',2],['*', 3],['/',3]]
# Initial Conditions:
operator_stack = []
input_stack = list(inp)
output_stack = []
lookahead = 0
operator_precedence = 0
current_precedence = 0
# Basic Definations
def operator_precedence(operator):
    n = operator_stack.index(operator)
    return allowed_operators[n][1]
# Program Begins Here:
for token in input_stack:
    try:
        int_token = int(token)
    except ValueError:
        if token in allowed_operators[:][0]:
            if operator_precedence(token) > current_precedence:
                operator_stack.insert(token)
            elif operator_stack(token) == current_precedence:
                n = operator_stack.pop()
                output_stack.append(n)
                operator_stack.append(token)
            else:
                for operator in operator_stack:
                    n = operator_stack.pop()
                    output_stack.append(n)
        else:
            raise OperatorNotValid(token)
    else:
        output_stack.append(int_token)
#Display Final Condition
print ("Final Stack looks as follows: \n", *output_stack)
