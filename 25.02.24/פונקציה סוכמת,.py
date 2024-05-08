def sum_all(the_list: list):
    s = 0
    for i in the_list:
        s = s + i
    print(s)


op = [5, 8, 9, 23, 3]
sum_all(op)


def registration(first_name, last_name, phone, email, password):
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Phone:", phone)
    print("Email:", email)
    print("Password:", password)


new_user = ["Yossi", "Levi", "056 - 5753572", "056575yl@gmail.com", "1234"]
registration(*new_user)
