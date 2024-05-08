def linear_search(a, n):
    if a[-1] == n:
        return True
    if len(a) == 1:
        return False
    return linear_search(a[:-1], n)

arr = [0, 1, 5, 7, 8, 10]
print(linear_search(arr, 5))
