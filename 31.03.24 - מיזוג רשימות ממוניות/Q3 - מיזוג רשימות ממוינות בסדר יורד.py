def reverse_merge(arr1, arr2):
    nl = []
    i1 = 0
    i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] > arr2[i2]:
            nl.append(arr1[i1])
            i1 += 1
        else:
            nl.append(arr2[i2])
            i2 += 1
    nl += arr1[i1:]
    nl += arr2[i2:]
    return nl

print(reverse_merge([14, 13, 10, 8, 6, 4], [12, 9, 5, 3]))

def reverse_sort_merge(array):
    if len(array) <= 1:
        return array
    half = len(array) // 2
    right = reverse_sort_merge(array[:half])
    left = reverse_sort_merge(array[half:])
    return reverse_merge(right, left)

print(reverse_sort_merge([5, 8, 9, 6, 7, 4, 8, 5, 2, 4]))