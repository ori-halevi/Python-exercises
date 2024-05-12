"""
מספר ראשוני הוא מתחלק ב1 ובעצמו בלבד! מספיק לבדוק כל מספר אם אינו מתחלק בכל המספרים עד השורש שלו אז הוא ראשוני
"""


def root(num: int) -> float:
    return num ** 0.5


def chak_for_foo(num):
    h = int(root(num))
    for i in range(2, h + 1):
        if not num % i:  # If this number divided even ones without a remainder, it's not prime number
            return False
    return True


def foo(range_: int):
    list_ = []
    for i in range(1, range_):
        if chak_for_foo(i):
            list_.append(i)
    return list_


selected_num = 9
print(foo(10))
