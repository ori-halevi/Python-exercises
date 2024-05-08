def multiplication(first_num: int, second_num: int) -> int:
    result = first_num * second_num
    return result


def factorial(num):
    foo = 1
    for i in range(1, num + 1):
        foo = multiplication(foo, i)
    return foo


print(factorial(4))
