def multiplication_table(limit_num: int):
    for i in range(limit_num):
        line = multiplication_num_by_numbers(i, limit_num)
        print(line, end="")
        print()


def multiplication_num_by_numbers(main_num: int, numbers_up_to_: int):
    result = []
    for i in range(numbers_up_to_ + 1):
        result.append(main_num * i)
    return result



multiplication_table(10)
