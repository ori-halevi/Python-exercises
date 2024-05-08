"""
פונקציה רקורסיבית המקבלת מערך ומחזירה אמת אם המערך הוא מערך קבוע
k ואחרת שקר
"""
def k_array(a, k=0):
    if a[1] - a[0] != k and a[0] - a[1] != k:
        return False
    if len(a) == 2:
        return True
    return k_array(a[1:], k)


print(k_array([6, 8, 10, 12, 14], 2))                 # -> True
print(k_array([5, 8, 11, 14, 11, 14, 11, 8], 3))      # -> True
print(k_array([8, 5, 4, 1], 3))                       # -> False
