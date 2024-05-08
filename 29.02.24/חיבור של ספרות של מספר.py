def sum_of_digits(number: int):
    number = list(str(number))
    result = 0
    for num in number:
        result += int(num)
    return result


result = sum_of_digits(123)
print(result)
