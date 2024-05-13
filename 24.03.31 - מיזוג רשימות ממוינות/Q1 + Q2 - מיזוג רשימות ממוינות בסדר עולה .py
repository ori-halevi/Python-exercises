# O(n log(n))

def merge_lists(first_list: list, second_list: list):
    merged_list = []
    first_list_idx, second_list_idx = 0, 0
    while first_list_idx < len(first_list) and second_list_idx < len(second_list):
        if first_list[first_list_idx] < second_list[second_list_idx]:
            merged_list.append(first_list[first_list_idx])
            first_list_idx += 1
        else:
            merged_list.append(second_list[second_list_idx])
            second_list_idx += 1
    merged_list += first_list[first_list_idx:]
    merged_list += second_list[second_list_idx:]
    return merged_list


my_first_list = [2, 5, 8]
my_second_list = [3, 6, 9, 12]
print(merge_lists(my_first_list, my_second_list))


def divide_and_merge(mixed_list: list):
    if len(mixed_list) <= 1:
        return mixed_list
    half = len(mixed_list) // 2
    right = divide_and_merge(mixed_list[:half])
    left = divide_and_merge(mixed_list[half:])
    return merge_lists(right, left)


my_mixed_list = [5, 7, 8, 5, 6, 1, 4, 2, 84, 74, 23, 12]
print(divide_and_merge(my_mixed_list))
