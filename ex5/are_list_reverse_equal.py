# שאלה 1:
# כתבו פונקציה המקבלת שני מערכים a, b.
# אם הערכים שבמערך a שווים לערכים שבמערך b אבל בסדר הפוך - פונקציה תחזיר True (ערך בוליאני). אחרת הפונקציה תחזיר False.
def are_list_reverse_equal(a, b):
    if a == b[::-1]:
        return True
    else:
        return False


# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestAreListReverseEqual(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, are_list_reverse_equal([3, 6, 7], [7, 6, 3]))

    def test_2(self):
        self.assertEqual(False, are_list_reverse_equal([3, 6], [7, 6, 3]))

    def test_3(self):
        self.assertEqual(False, are_list_reverse_equal([3, 1, 7], [7, 6, 3]))


if __name__ == '__main__':
    unittest.main()