def mul(a):
    if len(a) <= 1:
        return a[0]
    return a[-1] * mul(a[:-1])

print(mul([3, 4, 6]))
