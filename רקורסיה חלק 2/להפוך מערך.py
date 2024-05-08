def reverse(a, i=0):
    if len(a) // 2 == i:
        return a
    a[i], a[-i-1] = a[-i-1], a[i]
    return reverse(a, i + 1)

print(reverse([4, 8, 9, 4, 1, 0]))