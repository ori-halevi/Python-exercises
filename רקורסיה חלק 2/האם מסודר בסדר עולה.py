def is_sorted(a):
    if len(a) == 1:
        return True
    if a[-1] < a[-2]:
        return False
    return is_sorted(a[:-1])

arr = [0, 1, 5, 7, 8, 10]
print(is_sorted(arr))
