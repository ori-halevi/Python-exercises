ROUND_DOWN = 1
ROUND_UP = 2
ROUND = 3

user_num = float(input("Please enter a number: "))

print()
print("Choose your round method: ")
print("Floor round .1")
print("Ceiling round .2")
print("Round to the nearest whole number .3")

user_choice = int(input(">>> "))

if user_choice == 1 or user_choice == 2 or user_choice == 3:

    if user_choice == 1:
        output = user_num // 1

    elif user_choice == 2:
        if not user_num % 1 == 0:
            output = (1 - (user_num % 1)) + user_num
        else:
            output = user_num

    elif user_choice == 3:
        if user_num % 1 < 0.5:
            output = user_num // 1
        else:
            output = (1 - (user_num % 1)) + user_num

    print(output)

else:

    print("Input not valid!")
    exit()
