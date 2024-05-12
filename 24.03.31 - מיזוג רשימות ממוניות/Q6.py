def merge(arr1, arr2):
    nl = []
    i1 = 0
    i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            nl.append(arr1[i1])
            i1 += 1
        else:
            nl.append(arr2[i2])
            i2 += 1
    nl += arr1[i1:]
    nl += arr2[i2:]
    return nl


def sort_merge(array):
    if len(array) <= 1:
        return array
    half = len(array) // 2
    right = sort_merge(array[:half])
    left = sort_merge(array[half:])
    return merge(right, left)

def convert_to_tuples_in_list(dic_list: list):
    new_list = []
    for dic in dic_list:
        for key, value in dic.items():
            new_list.append((key, value))
    return new_list



lst_of_dic = [{"a" : 100 ,"zohar" : 1}, {"ronen" : 3, "noa" : 5, "ori" : 100}, {"david" : 80, "moshe" : 90}]

first_step = convert_to_tuples_in_list(lst_of_dic)
second_step = sort_merge(first_step)

print(second_step)
