import time

def swap(array: list, index_a, index_b):
    array[index_a], array[index_b] = array[index_b], array[index_a]
    return array


def is_bigger(first_n: float | int, second_n: float | int):
    if first_n > second_n:
        return True
    else:
        return False


def is_smaller(first_n: float | int, second_n: float | int):
    if first_n < second_n:
        return True
    else:
        return False


def print_result(list_type: str, original_array: list, sorting_type, sorted_array: list, loops: int):
    text = f"""
    The list type:          {list_type}.
    The original list:      {original_array}.
    The sorting type:       {sorting_type}.
    The sorted list:        {sorted_array}.
    The number of loops:    {loops}.
    """
    return print(text, end="")


""" sorting functions: """
def linear_sort(array: list):
    loop_summary = 0
    for i in range(len(array)):
        index = i
        while index > 0 and array[index - 1] > array[index]:
            loop_summary += 1
            swap(array, index, index - 1)
            index -= 1
    return array, loop_summary


def classic_bubble_sort(array: list):
    loop_summary = 0
    for j in range(len(array)):
        for i in range(len(array) - j - 1):
            loop_summary += 1
            if is_bigger(array[i], array[i + 1]):
                swap(array, i, i + 1)
    return array, loop_summary


def to_middle_sort(array: list):
    loop_summary = 0
    for j in range((len(array)) // 2):
        is_sorted = True
        index = j
        while index < len(array) - 1 - j:
            loop_summary += 1
            if is_bigger(array[index], array[index + 1]):
                swap(array, index, index + 1)
                is_sorted = False
            index += 1
        index = j + 1
        if is_sorted:
            break
        is_sorted = True
        while len(array) - 1 - index >= j:
            loop_summary += 1
            if is_smaller(array[len(array) - index], array[len(array) - 1 - index]):
                swap(array, len(array) - index, len(array) - 1 - index)
                is_sorted = False
            index += 1
        if is_sorted:
            break
    return array, loop_summary
# more sorting functions #


""" arrays: """
nearly_sorted_array = [1, 2, 4, 5, 3, 6, 7, 8, 9]
random_array = [5, 2, 8, 1, 3, 7, 4, 6, 9]


def measure_sort_efficiency(sort_function, array):
    start_time = time.time()
    sorted_array, loop_summary = sort_function(array.copy())
    end_time = time.time()

    print(f"Sort function: {sort_function.__name__}")
    print(f"Time taken: {end_time - start_time: .10000f} seconds")
    print(f"Loop iterations: {loop_summary}")
    print()



def organised_array():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return array


def revers_array():
    array = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    return array



def switched_array():
    array = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]
    return array


def start_to_end_array():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 16, 17, 18, 19, 0]
    return array


def random1_array():
    array = [0, 18, 19, 14, 4, 7, 10, 12, 2, 11, 16, 8, 9, 15, 13, 17, 1, 3, 5, 6, 20]
    return array



"""organised array"""
#
# sorted_array, loop_summary = linear_sort(organised_array())
# print_result("organised list", organised_array(), "linear_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = classic_bubble_sort(organised_array())
# print_result("organised list", organised_array(), "classic_bubble_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = to_middle_sort(organised_array())
# print_result("organised list", organised_array(), "to_middle_sort", sorted_array, loop_summary)

"""revers array"""
# sorted_array, loop_summary = linear_sort(revers_array())
# print_result("reversed list", revers_array(), "linear_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = classic_bubble_sort(revers_array())
# print_result("reversed list", revers_array(), "classic_bubble_sort", sorted_array, loop_summary)

# sorted_array, loop_summary = to_middle_sort(revers_array())
# print_result("reversed list", revers_array(), "to_middle_sort", sorted_array, loop_summary)


"""switched array"""
# sorted_array, loop_summary = linear_sort(switched_array())
# print_result("switched list", switched_array(), "linear_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = classic_bubble_sort(switched_array())
# print_result("switched list", switched_array(), "classic_bubble_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = to_middle_sort(switched_array())
# print_result("switched list", switched_array(), "to_middle_sort", sorted_array, loop_summary)


"""random array"""
# sorted_array, loop_summary = linear_sort(random_array())
# print_result("random list", random_array(), "linear_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = classic_bubble_sort(random_array())
# print_result("random list", random_array(), "classic_bubble_sort", sorted_array, loop_summary)

# sorted_array, loop_summary = to_middle_sort(random_array())
# print_result("random list", random_array(), "to_middle_sort", sorted_array, loop_summary)

""" start to end """
# sorted_array, loop_summary = linear_sort(start_to_end_array())
# print_result("start_to_end_array list", start_to_end_array(), "linear_sort", sorted_array, loop_summary)
#
# sorted_array, loop_summary = classic_bubble_sort(start_to_end_array())
# print_result("start_to_end_array list", start_to_end_array(), "classic_bubble_sort", sorted_array, loop_summary)

# sorted_array, loop_summary = to_middle_sort(start_to_end_array())
# print_result("start_to_end_array list", start_to_end_array(), "to_middle_sort", sorted_array, loop_summary)


# נניח שכבר יש לך את הפונקציות linear_sort ו-classic_bubble_sort מוגדרות כראוי
measure_sort_efficiency(linear_sort, nearly_sorted_array)
measure_sort_efficiency(classic_bubble_sort, nearly_sorted_array)

measure_sort_efficiency(linear_sort, random_array)
measure_sort_efficiency(classic_bubble_sort, random_array)


