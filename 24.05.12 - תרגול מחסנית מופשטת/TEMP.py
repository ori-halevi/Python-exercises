def cal_max(l: list):
    if l:
        f = l[0]
        for i in range(len(l)):
            if l[i] > f:
                f = l[i]
        return f
def cal_average(l: list):
    if l:
        f = 0
        for i in l:
            f += l
        return f // len(l)

