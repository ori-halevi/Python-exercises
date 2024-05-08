
def palindrome(any_array: list) -> None:
    print(any_array[0], end=" ")
    if len(any_array) > 1:
        palindrome(any_array[1:])
    print(any_array[0], end=" ")


if __name__ == "__main__":
    my_stupid_array = [20, 30, 50, 60]
    palindrome(my_stupid_array)  # -> 5

