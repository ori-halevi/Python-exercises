def swap(array: list, index_a, index_b):
    array[index_a], array[index_b] = array[index_b], array[index_a]
    return array

def cocktail_sort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start = start + 1
    return array
a = [5, 1, 4, 2, 8, 0, 2]
t = cocktail_sort(a)
print(t)
