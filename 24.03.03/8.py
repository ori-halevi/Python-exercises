def print_lists(list: list):
    for g in list:
        print(g, end=" ")


new_list = [0]
count = 6
for i in range(6):
    for g in range(count):
        print(end=" ")
    print_lists(new_list[::-1])
    print_lists(new_list[1:])
    print()
    count -= 1
    new_list.append(i + 1)
