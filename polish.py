# DCP 163
# Given an arithmetic expression in Reverse Polish notation,
# write a program to evaluate it. (https://en.wikipedia.org/wiki/Reverse_Polish_notation).
def polish(chars):
    stack = []
    
    for char in chars:
        if char in ["+", "-", "/", "*"]:
            b = stack.pop()
            a = stack.pop()
            if char == "+":
                stack.append(a + b)
            elif char == "-":
                stack.append(a - b)
            elif char == "/":
                stack.append(a / b)
            elif char == "*":
                stack.append(a * b)
        else:
            stack.append(char)

    return stack.pop()
