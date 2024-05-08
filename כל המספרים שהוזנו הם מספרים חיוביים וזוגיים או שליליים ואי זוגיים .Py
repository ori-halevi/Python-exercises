my_input_counting_array = ["first", "second", "third", "fourth"]
user_numbers = []
user_numbers_addition = 0
all_positive = False
all_even = False

for i in range(len(my_input_counting_array)):
    # asking from the user an input
    user_numbers.append(input("Please type your " + my_input_counting_array[i] + " integer: "))

    # If the user put anything but integer or put nothing in the input - it will be replaced with 0
    if not user_numbers[i].lstrip('-').isdigit():
        user_numbers[i] = "0"

print(
    (int(user_numbers[0]) > 0 and int(user_numbers[0]) % 2 == 0) and
    (int(user_numbers[1]) > 0 and int(user_numbers[1]) % 2 == 0) and
    (int(user_numbers[2]) > 0 and int(user_numbers[2]) % 2 == 0) and
    (int(user_numbers[3]) > 0 and int(user_numbers[3]) % 2 == 0)
    or
    (int(user_numbers[0]) < 0 and int(user_numbers[0]) % 2 == 1) and
    (int(user_numbers[1]) < 0 and int(user_numbers[1]) % 2 == 1) and
    (int(user_numbers[2]) < 0 and int(user_numbers[2]) % 2 == 1) and
    (int(user_numbers[3]) < 0 and int(user_numbers[3]) % 2 == 1)
)
print()

print(
    "is zero exist =",
    (int(user_numbers[0]) == 0) or
    (int(user_numbers[1]) == 0) or
    (int(user_numbers[2]) == 0) or
    (int(user_numbers[3]) == 0),
)

