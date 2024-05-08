# שאלה 2:
# כתבו פונקציה המקבלת שני מערכים באורך זהה (אין צורך לוודא) של מספרים - a, b.
# הפונקציה תחזיר True (ערך בוליאני) אם כל אינדקס,
# האיבר באותו האינדקס במערך b גדול ממש מהאיבר המקביל במערך a. אחרת הפונקציה תחזיר False.
def is_list_greater_then(a, b):
    all_big = True
    for i in range(len(a)):
        if b[i] <= a[i]:
            all_big = False
            break
    return all_big


# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestAreListReverseEqual(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, is_list_greater_then([3,2], [4,3]))

    def test_2(self):
        self.assertEqual(True, is_list_greater_then([3, 2], [5, 30]))

    def test_3(self):
        self.assertEqual(True, is_list_greater_then([3], [4]))

    def test_4(self):
        self.assertEqual(False, is_list_greater_then([3, 4, 5], [4, 5, 5]))

if __name__ == '__main__':
    unittest.main()