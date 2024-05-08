user_num = input("Please enter a number between 1 to 7: ")
user_num = int(user_num)

if user_num == 7 or user_num <= 1:
    user_num = input("Please enter a number between 1 to 7: ")

if user_num == 2 or user_num == 3 or user_num == 5 or user_num == 7:
    print(1)
else:
    print(0)


