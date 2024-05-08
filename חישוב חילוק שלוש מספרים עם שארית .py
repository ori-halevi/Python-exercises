num1 = 8
num2 = 4
num3 = 2

all_numbers = num1, num2, num3

for num1 in all_numbers:
    for num2 in all_numbers:
        dev = num1 / num2
        mod = num1 % num2
        print(str(num1) + "/" + str(num2) + " = " + str(dev) + "    " + str(num1) + "%" + str(num2) + " = " + str(mod))
