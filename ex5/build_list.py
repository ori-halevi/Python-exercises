# שאלה 5:
# כתבו פונקציה המקבל מערך של מספרים באורך גדול מחמש (אין צורך לוודא) a.
# הפונקציה תחזיר מערך חדש המכיל
# חמשת הערכים הראשונים הם הערכים באותו מיקום בa כפול 2.
# יתרת הערכים עד שהאיבר בa הינו מספר שלילי (לא כולל), יהיו הערכים באותו מיקום בa כפול 3.
# שאר הערכים בa יועתקו לקצה המערך החדש ללא שינוי.

def build_list(a):
    new_lst = []
    end_point = 0
    for i in range(len(a)):
        if i < 5:
            new_lst.append(a[i] * 2)
        elif a[i] < 0:
            end_point = i
            break
        else:
            new_lst.append(a[i] * 3)
    new_lst += a[end_point:]
    return new_lst


# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestAreListReverseEqual(unittest.TestCase):
    def test_1(self):
        self.assertEqual([6, 4, 2, 10, 6, 15, 18, -1, 4, 5], build_list([3, 2, 1, 5, 3, 5, 6, -1, 4, 5]))


if __name__ == '__main__':
    unittest.main()
