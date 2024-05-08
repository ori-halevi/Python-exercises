ls = [2, 3, 4]
def power(lst: list) -> list:
    if len(lst) == 1:
        return lst[0]**2
    return power(lst[:-1])
print(power(ls))
"""
not working!
"""