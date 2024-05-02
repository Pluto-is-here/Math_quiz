import random
import math


def int_checker(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...

    if low is None and high is None:
        print()
        error = "Please enter an integer"
        print()

    # If the number needs to be more than an integer (ie: rounds / high number)

    elif low is not None and high is None:
        print()
        error = f"please enter an integer that is more than / equal to {low}"
        print()
    else:
        print()
        error = f"Please enter an integer that is between {low} and {high} inclusive"
        print()
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # if response is valid, return it

            # check the integer is not too low...
            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response
            # Checks that the number is more than / equal to 13

        except ValueError:
            print(error)


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print()
            print("Please choose either yes or no.")
            print()


def operation_checker(question):
    while True:

        op_wanted = input(question).lower()

        if op_wanted == "x":
            return "x"
        elif op_wanted == "+":
            return "+"
        elif op_wanted == "/":
            return "/"
        elif op_wanted == "-":
            return "-"
        elif op_wanted == "":
            return "all operations"
        else:
            print()
            print("I'm sorry, that is not a valid operation. Please choose x, (multiply), - (subtract),  / (divide) or"
                  "+ (add")
            print()


def instructions():
    print(''' 

    *** Instructions ***

    In this math quiz, you will test and improve your math skills. You may choose what type of operation
    you want to use ( + , - , x, and / (division))
    
    Type "xxx" if you want to quit midway through a quiz. 

    Good luck!
    ''')


# initialize quiz variables

mode = "regular"
end_quiz = "no"
questions_asked = 0
quiz_history = []
correct = 0
incorrect = 0

# assigning a number to a operation to generate a mix of equations

print()
print(" 🧮 Math Quiz 🧮")
print()

want_instructions = yes_no("Do you want to view instructions? ")

if want_instructions == "yes":
    instructions()

# setting quiz parameters

questions_wanted = int_checker("How many questions do you want? Push <enter> for infinite mode: ", low=1, exit_code="")
print()

# making sure that questions asked never equals questions answered for infinite mode

if questions_wanted == "":
    mode = "infinite"
    questions_wanted = 10

operation = operation_checker("What operation do you want your questions to be? ")

print()
default_setting = yes_no("Do you want to use the default range? (1-10)\t"
                         "(Note: For division mode, this means that the answers will be between 1-10) ")

if default_setting == "yes":
    low_num = 1
    high_num = 10
else:
    low_num = int_checker("Choose a minimum number: ")
    high_num = int_checker("Choose a maximum number: ", low=low_num + 1)

# main quiz loop starts here.

while questions_asked < questions_wanted:

    if mode == "infinite":
        rounds_heading = f"\n ♾♾♾ Question {questions_asked + 1} (Infinite mode) ♾♾♾"
        questions_wanted += 1
    else:
        rounds_heading = f"\n 🕰🕰🕰 Question {questions_asked + 1} / {questions_wanted} 🕰🕰🕰 "

    print(rounds_heading)
    print()

    # generate equation / the equation

    equation_num1 = random.randint(low_num, high_num)
    equation_num2 = random.randint(low_num, high_num)

    # Generating questions for the user to read
    # Making sure that division questions are always integers
    if operation == "/":
        for_div = equation_num1 * equation_num2
        ask_equ = f"{for_div} / {equation_num2}"
        # Making it so that subtraction question answers are always positive
    elif operation == "-":
        if equation_num2 >= equation_num1:
            ask_equ = f"{equation_num2} {operation} {equation_num1}"
        else:
            ask_equ = f"{equation_num1} {operation} {equation_num2}"
    else:
        ask_equ = f"{equation_num1} {operation} {equation_num2}"

    # generating the questions in a way that the computer can solve them (to get answers to check against)

    if operation == "x":
        solve_equ = equation_num1 * equation_num2
    elif operation == "-":
        if equation_num2 >= equation_num1:
            solve_equ = equation_num2 - equation_num1
        else:
            solve_equ = equation_num1 - equation_num2
    elif operation == "/":
        solve_equ = for_div / equation_num2
    elif operation == "+":
        solve_equ = equation_num1 + equation_num2

    # asking user question for input

    user_input = int_checker(f"What's {ask_equ}? ", low=0, exit_code="xxx")
    print()
    # user feedback on right/wrong answer

    if user_input == "xxx":
        end_quiz = "yes"
        break

    elif user_input != solve_equ:
        print()
        print(f" I'm sorry, that's wrong. The answer is {solve_equ:.0f} .")
        incorrect += 1
        quiz_history.append(f"❌ Question {questions_asked + 1}: {ask_equ} : Wrong! The answer was {solve_equ:.0f}")

    elif user_input == solve_equ:
        print()
        print("Correct!")
        correct += 1
        quiz_history.append(f"✅ Question {questions_asked + 1}: {ask_equ} : Right! The answer was {solve_equ:.0f}")

    questions_asked += 1

# quiz loop ends here

# calculating quiz stats
if questions_asked == questions_wanted or end_quiz == "yes" and questions_asked > 0:

    total_correct = correct
    total_incorrect = incorrect
    success_rate = correct / questions_asked * 100

    print()
    print("📈 Quiz Stats 📉")
    print()
    print()
    print(f"Total Correct = {total_correct} |\t"
          f"Total Wrong = {total_incorrect} |\t"
          f"Success Rate = {success_rate:.0f}%")
    print()

    # optional history of quiz w/ right or wrong answers

    want_history = yes_no("Do you want to view your quiz history? ")

    if want_history == "yes":

        print()

        for item in quiz_history:
            print(item)

    print()
    print("Thank you for playing!")

else:
    print("Goodbye!")

    # num_1 < generated > = 3
    # num_2 < generated > = 4
    # answer = 12
    #
    # for division
    #     'answer' / num_1 = 4
