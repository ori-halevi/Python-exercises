def fibonacci_sequence(loop):
    start = [0, 1]
    for i in range(loop):
        for g in range(len(start)):
            if g != 0:
                print(start[g], end=" ")
        print()

        start.append(start[i] + start[i + 1])


fibonacci_sequence(4)
