
def sort_by_merge(array: list) -> list:
    """
    This function work time in complexity of O(n log(n))
    :param array:
    :return: sorted list.
    """
    if len(array) <= 1:
        return array
    half = len(array) // 2
    right_side = sort_by_merge(array[:half])
    left_side = sort_by_merge(array[half:])

    merge_list = []
    first_list_idx = 0
    second_list_idx = 0
    while first_list_idx < len(right_side) and second_list_idx < len(left_side):
        if right_side[first_list_idx] < left_side[second_list_idx]:
            merge_list.append(right_side[first_list_idx])
            first_list_idx += 1
        else:
            merge_list.append(left_side[second_list_idx])
            second_list_idx += 1
    merge_list += right_side[first_list_idx:]
    merge_list += left_side[second_list_idx:]
    return merge_list


if __name__ in "__main__":
    my_not_sorted_list = [50, 70, 40, 60, 80]
    print(sort_by_merge(my_not_sorted_list))
