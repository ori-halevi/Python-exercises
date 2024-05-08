
def hanoi(n, start, end):
    if n == 1:
        print(start, "->", end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print(start, "->", end)
        hanoi(n - 1, other, end)

hanoi(2, 1, 3)
