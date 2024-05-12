
e = [1,2,3,4]

def sum_of_array(lst: list):
    if len(lst) == 1:
        return lst[0]
    return sum_of_array(lst[:-1]) + lst[-1]

print(sum_of_array(e))