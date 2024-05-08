
def merge(first_list: list, second_list: list) -> list:
    merge_list = []
    inx_in_first_list, inx_in_second_list = 0, 0
    while inx_in_first_list < len(first_list) and inx_in_second_list < len(second_list):
        if first_list[inx_in_first_list] < second_list[inx_in_second_list]:
            merge_list.append(first_list[inx_in_first_list])
            inx_in_first_list += 1
        else:
            merge_list.append(second_list[inx_in_second_list])
            inx_in_second_list += 1
    merge_list += first_list[inx_in_first_list:]
    merge_list += second_list[inx_in_second_list:]
    return merge_list


def sort_by_merge(array: list) -> list:
    """
    This function work time in complexity of O(n log(n))
    :param array:
    :return: sorted list.
    """
    if len(array) <= 1:
        return array
    half = len(array) // 2
    right_side = array[:half]
    left_side = array[half:]
    return merge(right_side, left_side)


if __name__ in "__main__":
    my_not_sorted_list = [50, 70, 40, 60, 80]
    print(sort_by_merge(my_not_sorted_list))
