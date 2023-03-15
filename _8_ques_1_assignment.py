"""Reverse a string using a stack data structure"""

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# get user input for the string
s = input("Enter a string: ")

# call the reverse_string function on the string
reversed_string = reverse_string(s)

# print the reversed string
print("The reversed string is:", reversed_string)
