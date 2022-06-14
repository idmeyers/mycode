#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your score means '

def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("User input is Number")
        return True
    else:
        print("User input is string")
        return False
# wrap connection in a float() to accept decimals as numbers
score = (input("What is your score?"))
if check_is_digit(score):
    score = float(score) 
# if input value was higher or equal to 25
    if score >= 90:
        message = message + 'that you received an A.'
    elif score >= 80:
        message = message + 'that you received a B.'
    elif score >= 70:
        message = message + 'that you received a C.'
    elif score >= 60:
        message = message + 'that you received a D.'
    elif score >= 0:
        message = message + 'that you failed and need to study more.'
    else:
        message = message + 'that you did not actually take a test.'

else:
    message = message + 'that you did not actually take a test.'

print(message)

