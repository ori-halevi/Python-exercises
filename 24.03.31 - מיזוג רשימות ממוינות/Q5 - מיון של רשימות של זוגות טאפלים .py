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

print(sort_merge([(5, 8), (9, 6), (7, 4), (8, 5), (2, 4)]))