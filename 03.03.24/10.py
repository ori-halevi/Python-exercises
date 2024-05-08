def print_down_hil_pyramid(any_note: str, replacement_character: str, base_size: int):
    for current_line in range(1, base_size):
        if current_line == 1:
            print_duplicate_char_by_num(any_note, base_size)
            print()
        else:
            print_one_line_with_replacement_char(any_note, replacement_character, current_line)
            print_one_line_with_replaced_char(any_note, replacement_character, base_size - current_line)
            print()
        if current_line == base_size - 1:
            print_duplicate_char_by_num(any_note, base_size)


def print_duplicate_char_by_num(char: str, repeat: int):
    for h in range(repeat):
        print(char, end=" ")


def print_one_line_with_replacement_char(any_note: str, replacement_character: str, line_length: int):
    """
    This function will print a line of two characters each one in its turn,
    This function also deside to choose the first character depends on if the length of the line is even or odd,
    If it's even it will start with the replacement character, else, with the main note.
    :param any_note:
    :param replacement_character:
    :param line_length:
    :return:
    """
    for g in range(line_length):
        if g % 2 != 0 and line_length % 2 == 0 or line_length % 2 != 0 and g % 2 == 0:
            print(any_note, end=" ")
        else:
            print(replacement_character, end=" ")


def print_one_line_with_replaced_char(any_note: str, replacement_character: str, line_length: int):
    for i in range(line_length):
        if i % 2 != 0:
            print(any_note, end=" ")
        else:
            print(replacement_character, end=" ")


print_down_hil_pyramid("-", "+", 5)
