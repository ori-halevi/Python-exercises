def multiplication(f_num, s_num):
    return f_num * s_num


for i in range(5):
    rounds1 = i + 1
    for g in range(5):
        rounds2 = g + 1
        print(multiplication(rounds1, rounds2))
