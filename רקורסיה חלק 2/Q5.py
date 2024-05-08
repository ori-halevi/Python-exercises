def count(a1, a2, i=0):
    if i >= len(a1):
        return True
    if len(str(a1[i])) != a2[i]:
        return False
    return count(a1, a2, i + 1)

a1 = [10, 2, 58]
a2 = [2, 1, 2]
print(count(a1, a2))

a1 = [10, 2, 8]
a2 = [2, 1, 2]
print(count(a1, a2))

a1 = [10, 2, 843]
a2 = [2, 1, 2]
print(count(a1, a2))
