# O(n)
def linear_index_search(array: list, num: int) -> int:
    """
    This function work time in complexity of O(n)
    :param array:
    :param num:
    :return: index of the num in the array, it will return -1 if num does not exist.
    """
    for idx, elem in enumerate(array):
        if elem == num:
            return idx
    return -1


if __name__ in "__main__":
    my_sorted_list = [20, 30, 40, 50, 60]
    print(linear_index_search(my_sorted_list, 50))
