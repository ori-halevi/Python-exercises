# O(log(n))
def binary_index_search(array: list, num_to_search: int) -> int:
    """
    This function work time in complexity of O(log(n))
    :param array:
    :param num_to_search:
    :return: index of the num in the array, it will return -1 if num does not exist.
    """
    low_idx = 0
    high_idx = len(array) - 1
    while low_idx < high_idx:
        middle = (low_idx + high_idx) // 2
        if num_to_search == array[middle]:
            return middle
        elif num_to_search < array[middle]:
            high_idx = middle - 1
        else:
            low_idx = middle + 1
    return -1





if __name__ in "__main__":
    my_sorted_list = [20, 30, 40, 50, 60]
    print(binary_index_search(my_sorted_list, 50))
