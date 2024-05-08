"""
in this project I consider 0 as negative.
"""

my_input_counting_array = ["first", "second", "third", "fourth", "fifth"]
user_numbers = []
user_numbers_addition = 0

for i in range(len(my_input_counting_array)):
    # asking from the user an input
    user_numbers.append(input("Please type your " + my_input_counting_array[i] + " number: "))

    # If the user put anything but integer or put nothing in the input - it will be replaced with 0
    if not user_numbers[i].lstrip('-').isdigit():
        user_numbers[i] = "0"

for i in range(len(user_numbers)):
    # Check for negative and positive
    if int(user_numbers[i]) > 0:
        negative_or_positive = "positive"
    else:
        negative_or_positive = "negative"

    # Check rather if the number is odd or even:
    if not int(user_numbers[i]) % 2:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    # print the numer of the user
    print("your", my_input_counting_array[i], "number is: " + user_numbers[i]+",", "which is an", even_or_odd, "and", negative_or_positive, "number.")


# Calculating the average of the numbers
total = sum(map(int, user_numbers)) # בשורה זאת נעזרתי בAI
average = total / len(user_numbers)

# print the average:
print("")
print("The average of your numbers is: ", average)
