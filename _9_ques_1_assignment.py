"""Evaluate a postfix expression using stack"""

def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()
            if char == "+":
                result = first_operand + second_operand
            elif char == "-":
                result = first_operand - second_operand
            elif char == "*":
                result = first_operand * second_operand
            elif char == "/":
                result = first_operand / second_operand
            stack.append(result)

    return stack.pop()

# get user input for the postfix expression
expression = input("Enter a postfix expression: ")

# call the evaluate_postfix function on the expression
result = evaluate_postfix(expression)

# print the result of the postfix expression
print("The result of the postfix expression is:", result)
