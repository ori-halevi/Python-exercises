import random

def start_tirgul(some_str):
    """
    זמן ריצה 1
    סדר גודל O(1)
    """
    print("start tirgul")
    print(some_str)
    print("bye")
def not_zero_or_5(a):
    """
        זמן ריצה N
    סדר גודל O(N)
    """
    b = []
    n = len(a)
    for i in range(n):
        if i != 0 and i != 5:
            b.append(a[i])
    return b
def check_if_all_divisiable(nums1, num2):
    """
        זמן ריצה N בריבוע
    סדר גודל O(N בריבוע)
    """
    for n1 in nums1:
        for n2 in num2:
            divisable = n1 % n2 > 0
            if divisable:
                return False
    return True
def count_divisable(nums1):
    """
        זמן ריצה N*10000
    סדר גודל O(N)
    :param a:
    :return:
    """
    num2 = list(range(10000))
    count = 0
    for n1 in nums1:
        for n2 in num2:
            if n1 % n2 == 0:
                count += 1
    return count
def print_many(a):
    """
        זמן ריצה 10000
    סדר גודל O(10000)
    :param a:
    :return:
    """
    for i in range(10000):
        print(a)
def print_rnd(a):
    """
        זמן ריצה 0-999
    סדר גודל O(10000)
    :param a:
    :return:
    """
    n = random.randrange(10000)
    for i in range(n):
        print(a)
        print("a")
def print_limit_couple(a):
    """
        זמן ריצה a
    סדר גודל O(N)
    :param a:
    :return:
    """
    print("‘print limit’")
    print("‘start printing’")
    for i in range(len(a)):
        if i % 2:
            print(a[i])
def print_limit(a):
    """
        זמן ריצה a
    סדר גודל O(N)
    :param a:
    :return:
    """
    print("‘print limit’")
    print("‘start printing’")
    for i in range(len(a)):
        if i < 1000:
            print(a[i])
def print_limit_input(a, n):
    """
        זמן ריצה n
    סדר גודל O(N)
    :param a:
    :return:
    """
    i = 0
    while i < n:
        print(a[i])
        i += 1

def print_interesting(a):

    """
    שאלת הבונוס:
            זמן ריצה: אקפוננציאלי
        סדר גודל O(2**N)

    """
    index = 2
    exponent = 0
    while index < len(a):
        print(a[index])
        exponent += 1
        index = index ** exponent
