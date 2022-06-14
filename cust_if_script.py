#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your score means '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your score?"))

# if input value was higher or equal to 25
if connection >= 90:
    message = message + 'that you received an A.'
elif connection >= 80:
    message = message + 'that you received a B.'
elif connection >= 70:
    message = message + 'that you received a C.'
elif connection >= 60:
    message = message + 'that you received a D.'
elif connection >= 0:
    message = message + 'that you failed and need to study more.'
else:
    message = message + 'that you did not actually take a test.'
print(message)

