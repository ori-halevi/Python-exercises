first_num = input("Please enter your first number: ")
second_num = input("Please enter your second number: ")
third_num = input("Please enter your third number: ")
first_num = int(first_num)
second_num = int(second_num)
third_num = int(third_num)

if first_num > second_num and second_num > third_num:
    print("Order goes down")
elif first_num < second_num and second_num < third_num:
    print("Order goes up")
else:
    print("Order mix up")