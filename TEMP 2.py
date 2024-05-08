# def recorsiv_power(a, b):
#     if b == 0:
#         return 1
#     if b % 2 == 0:
#         return recorsiv_power(a * a, b // 2)
#     else:
#         return a * recorsiv_power(a, b - 1)
#
# print(recorsiv_power(2, 8))
# print()
#
# def search3(L, e):
#     if L[0] == e:
#         return True
#     elif L[0] > e:
#         return False
#     else:
#         return search3(L[1:], e)
#
# print(search3([1, 2, 3], 5))
#
#
#


# O(log n)
def binary(n):
    if n == 0:
        # print(0, end="")
        return
    b = n % 2
    binary(n // 2)
    print(b, end="")

binary(10)

