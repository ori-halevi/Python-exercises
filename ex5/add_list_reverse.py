# שאלה 3:
# כתבו פונקציה המקבלת שני מערכים באורך זהה (אין צורך לוודא) של מספרים - a, b.
# הפונקציה תחזיר מערך חדש בו
# במקום הראשון סכום האיבר הראשון ב-a והאיבר האחרון ב-b,
# במקום השני סכום האיבר השני ב-a והאיבר לפני האחרון ב-b
# וכך הלאה עד לסוף המערכים
def add_list_reverse(a, b):
    first_lst = a
    second_lst = b[::-1]
    new_lst = list()
    for i in range(len(first_lst)):
        new_lst.append(first_lst[i] + second_lst[i])
    return new_lst


# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestAreListReverseEqual(unittest.TestCase):
    def test_1(self):
        self.assertEqual([6, 6], add_list_reverse([3, 2], [4, 3]))

    def test_2(self):
        self.assertEqual([33, 7], add_list_reverse([3, 2], [5, 30]))

    def test_3(self):
        self.assertEqual([7], add_list_reverse([3], [4]))


if __name__ == '__main__':
    unittest.main()