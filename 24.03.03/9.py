def print_line(any_list: list, column: int):
    for i in range(column):
        print(any_list[i], end=" ")
    print()


def print_down_hil_pyramid(any_list: list, rows: int):
    for i in range(1, rows + 1):
        print_line(any_list, i)


def print_up_hil_pyramid(any_list: list, rows: int):
    for i in range(rows, 0, -1):
        print_line(any_list, i)



def print_kiss_vertices_pyramids(any_list: list):
    print_up_hil_pyramid(any_list, len(any_list))
    print_down_hil_pyramid(any_list, len(any_list))


letters = ["A", "B", "C", "D", "E"]

print_kiss_vertices_pyramids(letters)
