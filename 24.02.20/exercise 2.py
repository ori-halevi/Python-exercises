y = 5
n = 5
g = 1
while y:
    for i in range(n):
        print(" ", end="")
    for i in range(g):
        print("*", end="")
    y = y - 1
    n = n - 1
    g = g + 2
    print()
