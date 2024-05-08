
def bubble_sort(array: list) -> list:
    """
    This function work time in complexity of O(n**2)
    :param array:
    :return: sorted list.
    """
    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j], array[j + 1]
    return array

if __name__ in "__main__":
    my_not_sorted_list = [50, 70, 40, 60, 90]
    print(bubble_sort(my_not_sorted_list))
