
def sort_by_select(array: list) -> list:
    """
    This function work time in complexity of O(n**2)
    :param array:
    :return: sorted list.
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
    return array


if __name__ in "__main__":
    my_not_sorted_list = [50, 70, 40, 60, 90]
    print(sort_by_select(my_not_sorted_list))
