
def fibonacci(index: int) -> int:
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)


if __name__ == "__main__":
    print(fibonacci(5))  # -> 5
