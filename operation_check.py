import random


def operation_checker(question):
    operation = input(question).lower()

    if operation == "x":
        return "x"
    elif operation == "/":
        return "-"
    elif operation == "-":
        return "x"
    else:
        print("I'm sorry, that is not a valid operation. Please choose x, (multiply), - (subtract), or / (divide)")

