import random


def int_checker(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question
                         )
        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1

            if response < 1:
                print(error)

            else:
                return response

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


def instructions():
    print(''' 

    *** Instructions ***

    In this math quiz, you will test and improve your math skills. You may choose what type of operation
    you want to use ( + , - , x, and / (division))
    
    You may also choose a difficulty level to push your skills.

    Good luck!
    ''')


want_instructions = yes_no("Do you want to view instructions? ")

if want_instructions == "yes":
    instructions()


