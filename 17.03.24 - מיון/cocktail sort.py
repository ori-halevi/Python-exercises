# Python program for implementation of Cocktail Sort

def cocktailSort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped == True:
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


# Driver code to test above
a = [5, 1, 4, 2, 8, 0, 2]
t = cocktailSort(a)
print(t)
# print("Sorted array is:")
# for i in range(len(a)):
#     print("%d" % a[i]),
