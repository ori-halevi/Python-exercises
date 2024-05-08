def binary_search(a, num):
    if len(a) == 0:
        return -1
    middle = len(a) // 2
    if a[middle] == num:
        return middle
    elif a[middle] > num:
        return binary_search(a[:middle], num)
    else:
        idx = binary_search(a[middle + 1:], num)
        if idx < 0:
            return idx
        else:
            return idx + middle

a = [1, 2, 3, 4, 8, 41, 50, 70]
print(binary_search(a, 5))
