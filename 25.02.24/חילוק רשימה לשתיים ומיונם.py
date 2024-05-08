def convert_to_int(any_list: list):
    converted_list = []
    for i in any_list:
        o = i
        try:
            o = float(o)
            if o.is_integer():
                o = int(o)
        except ValueError:
            continue
        finally:
            converted_list.append(str(o))
    return converted_list


def just_numbers(any_list):
    numbers_list = []
    for i in any_list:
        o = i
        try:
            o = float(o)
        except ValueError:
            continue
        finally:
            if isinstance(o, (float, int)):
                if o.is_integer():
                    o = int(o)
                numbers_list.append(o)
    return numbers_list


def calculate_average(any_list: list):
    numbers_list = just_numbers(any_list)
    if numbers_list:
        _sum = 0
        for i in numbers_list:
            _sum += int(i)
        average = _sum / len(numbers_list)
        return average


def add_average(any_list: list):
    if calculate_average(any_list):
        any_list.append(str(calculate_average(any_list)))
    return any_list


def calculate_max(any_list: list):
    numbers_list = just_numbers(any_list)
    return max(numbers_list)


def add_max(any_list: list):
    if calculate_max(any_list):
        any_list.append(str(calculate_max(any_list)))
    return any_list


def del_the_3_small_numbers(any_list: list):
    numbers_list = just_numbers(any_list)
    any_list = convert_to_int(any_list)
    for i in range(3):
        if len(numbers_list) > 1:
            any_list.remove(str(min(numbers_list)))
            numbers_list.remove(min(numbers_list))
    return any_list


_input = input("Please enter numbers: ")
input_list = []
while _input != "q":
    input_list.append(_input)
    _input = input("Please enter numbers: ")

first_list = input_list[:len(input_list) // 2]
second_list = input_list[len(input_list) // 2:]


first_list = add_average(first_list)
first_list = add_max(first_list)
first_list = del_the_3_small_numbers(first_list)

second_list = add_average(second_list)
second_list = add_max(second_list)
second_list = del_the_3_small_numbers(second_list)


print(f"""
The first list is: {first_list}, 
Thr second list is: {second_list}.""")
