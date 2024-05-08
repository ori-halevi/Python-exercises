def merge(first_array: list, second_list: list) -> list:
    first_a_idx, sec_a_idx = 0, 0
    merge_list = []
    while first_a_idx < len(first_array) and sec_a_idx < len(second_list):
        if first_array[first_a_idx] > second_list[sec_a_idx]:
            merge_list.append(first_array[first_a_idx])
            first_a_idx += 1
        else:
            merge_list.append(second_list[sec_a_idx])
            sec_a_idx += 1
    merge_list += first_array[first_a_idx:]
    merge_list += second_list[sec_a_idx:]
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
    right = sort_by_merge(array[half:])
    left = sort_by_merge(array[:half])
    return merge(right, left)

if __name__ in "__main__":
    my_not_sorted_list = [50, 70, 40, 60, 80]
    print(sort_by_merge(my_not_sorted_list))
