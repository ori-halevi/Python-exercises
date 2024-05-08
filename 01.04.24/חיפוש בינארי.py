def binary_search(nums_list: list, num_to_search) -> int:
    low, high = 0, len(nums_list) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums_list[middle] == num_to_search:
            return middle
        elif nums_list[middle] < num_to_search:
            low = middle + 1
        else:
            high = middle - 1
    return -1


organized_list = [6, 8, 9, 10, 18, 20, 30]
print(binary_search(organized_list, 6))
