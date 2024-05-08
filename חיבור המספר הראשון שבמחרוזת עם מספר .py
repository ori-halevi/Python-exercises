my_str = input("Please enter a string: ")
my_str = my_str + "????"
num = int(input("Please enter a number: "))

new_str = 0
if my_str[0].isdigit():
    new_str = my_str[0]
    if my_str[1].isdigit():
        new_str = my_str[0:2]
        if my_str[2].isdigit():
            new_str = my_str[0:3]
            if my_str[3].isdigit():
                new_str = my_str[0:4]

result = int(new_str) + num

print(result)


