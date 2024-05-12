def prime(num):
    if num == 2:
        return num
    return prime(num)

def is_prime_recursive(number, divisor=None):
    if number <= 1:
        return False  # מספרים שליליים, 0 ו-1 אינם ראשוניים

    if divisor is None:
        divisor = number - 1  # התחל מהמחלק המקסימלי האפשרי שאינו המספר עצמו
    elif divisor == 1:
        return True  # הגענו לבדיקת המחלק האחרון ולא מצאנו מחלק שאינו 1 והמספר עצמו

    if number % divisor == 0:  # אם המספר מתחלק במחלק נוכחי, הוא אינו ראשוני
        return False
    return is_prime_recursive(number, divisor - 1)  # בצע בדיקה רקורסיבית עם המחלק הבא

# דוגמאות לשימוש בפונקציה
print(is_prime_recursive(29))  # True
print(is_prime_recursive(10))  # False

# def is_prime(number):
#     if number <= 1:
#         return False
#
#     for i in range(2, number):
#         if number % i == 0:
#             return False  # מצאנו מחלק שאינו המספר עצמו ו-1, לכן המספר אינו ראשוני
#     return True  # המספר הוא ראשוני אם לא מצאנו מחלקים אחרים
#
# # דוגמא לשימוש:
# print(is_prime(29))
# print(is_prime(8))
