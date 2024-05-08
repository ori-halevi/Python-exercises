user_input = input("Please enter a string: ")

if len(user_input) < 5:
    ratio = len(user_input) - 5
    user_input = user_input[:ratio + 1] + user_input
    print(user_input)

user_input_in_lower = user_input.lower()
print(user_input_in_lower)
letter_got_change = 0
if user_input[0] < user_input_in_lower[0]:
    letter_got_change = 1
if user_input[1] < user_input_in_lower[1]:
    letter_got_change += 1
if user_input[2] < user_input_in_lower[2]:
    letter_got_change += 1
if user_input[3] < user_input_in_lower[3]:
    letter_got_change += 1
if user_input[4] < user_input_in_lower[4]:
    letter_got_change += 1

print(letter_got_change)
