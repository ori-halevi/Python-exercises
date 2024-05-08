def linear_search(sorted_list: list, num_to_search) -> int|float:
    for i in range(len(sorted_list)):
        if sorted_list[i] == num_to_search:
            return i


organized_list = [6, 8, 9, 10, 18, 20, 30]
print(linear_search(organized_list, 10))
