"""
im not sure if understand the task so I explained every line's outcome.
"""

user_number = input("Insert a number: ")
user_number = int(user_number)
x = user_number < 0                     # x is the bool value of if the user number is positive or negative, (True = negative)
y = 2 * user_number > user_number       # y is the bool value of if the user number is 0, (True = not zero)
z = not x and not y                     # z is the bool value of if the user number is both positive and zero
print(not z or not user_number)         # if the user input is 0 or not 0, it will print True
