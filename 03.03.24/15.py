import random
def list_to_str(list_: list) -> str:
    return "".join(list_)


def random_nums(end_point):
    array_ = []
    for i in range(end_point):
        array_.append(str(random.randint(0, 999)))
    return array_


def full_string(num):
    a = random_nums(num)
    b = list_to_str(a)
    return b

user_input = int(input("Please enter a number: "))
rere = full_string(user_input)
print(rere)
