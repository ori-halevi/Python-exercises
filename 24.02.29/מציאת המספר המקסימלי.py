def find_max(list: list):
    max_number = list[0]
    for i in list:
        if max_number < i:
            max_number = i
    return max_number

mi = [8, 7, 54, 2]
print(find_max(mi))
print(max(mi))
