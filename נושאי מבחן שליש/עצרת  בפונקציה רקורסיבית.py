
def factorial(num: int) -> int:
    """
    This function will return the factorial of any number.
    :param num: number
    :return: factorial of num
    """
    if num <= 1:
        return num
    return num * factorial(num - 1)


if __name__ == "__main__":
    print(factorial(4))
