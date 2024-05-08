# כתבו פונקציה המקבלת שני מערכים באורך זהה (אין צורך לוודא) של מספרים - a, b.
# הפונקציה תחזיר מערך חדש בו
# באינדקסים האי-הזוגיים סכום האיברים באותו מקום ב-a והאיבר ב-b,
# באינדקסים זוגיים מכפלת האיברים באותו מקום ב-a והאיבר ב-b,
def build_alternating_list(a, b):
    new_lst = []
    for i in range(len(a)):
        if i % 2:
            new_lst.append(a[i] + b[i])
        else:
            new_lst.append(a[i] * b[i])
    return new_lst

# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestAreListReverseEqual(unittest.TestCase):
    def test_1(self):
        self.assertEqual([12,5,2], build_alternating_list([3,2,1], [4, 3, 2]))

    def test_2(self):
        self.assertEqual([15, 32], build_alternating_list([3, 2], [5, 30]))

    def test_3(self):
        self.assertEqual([12], build_alternating_list([3], [4]))


if __name__ == '__main__':
    unittest.main()
