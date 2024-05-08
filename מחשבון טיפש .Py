first_num = input("Please enter your first number: ")
second_num = input("Please enter your second number: ")
operator = input("Please enter your wanted operator")

first_num = int(first_num)
second_num = int(second_num)

if operator == "*":
    print("The result: ", first_num * second_num)

elif operator == "/":
    print("The result: ", first_num / second_num)

elif operator == "+":
    print("The result: ", first_num + second_num)

elif operator == "*":
    print("The result: ", first_num - second_num)

elif operator == "%":
    print("The result: ", first_num % second_num)

else:
    print("The operator is not valid")