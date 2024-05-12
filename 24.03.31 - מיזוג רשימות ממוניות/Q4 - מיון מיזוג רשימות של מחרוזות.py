def merge_string(f_str_list: list, s_str_list: list) -> list:
    new_str_list = list()
    i1, i2 = 0, 0
    while i1 < len(f_str_list) and i2 < len(s_str_list):
        if len(f_str_list[i1]) < len(s_str_list[i2]):
            new_str_list.append(f_str_list[i1])
            i1 += 1
        else:
            new_str_list.append(s_str_list[i2])
            i2 += 1

    new_str_list += f_str_list[i1:]
    new_str_list += s_str_list[i2:]
    return new_str_list

print(merge_string(["r", "wer", "uyttrr", "dfsfasaa"], ["rw", "wwer", "ueyttrr", "drrfsfasaa"]))

def string_sort_merge(str_list: list) -> list:
    if len(str_list) <= 1:
        return str_list
    half = len(str_list) // 2
    right = string_sort_merge(str_list[:half])
    left = string_sort_merge(str_list[half:])
    return merge_string(right, left)

print(string_sort_merge(["rwe", "rwgaas", "af", "a", "asdgf", "asdf", "234"]))