user_num1 = input("Please enter your first number: ")
user_num2 = input("Please enter your second number: ")
user_num3 = input("Please enter your third number: ")
user_num1 = float(user_num1)
user_num2 = float(user_num2)
user_num3 = float(user_num3)

if user_num1 > user_num2:
    biggest = user_num1
else:
    biggest = user_num2

if biggest > user_num3:
    biggest = biggest
else:
    biggest = user_num3

print("the biggest number is:", biggest)
