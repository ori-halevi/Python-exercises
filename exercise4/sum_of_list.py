# כתוב פונקציה המקבלת רשימת מספרים ומחזירה את סכומה
def sum_of_list(lst):
    f = 0
    for i in lst:
        f += i
    return f


# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestSumOfListRecursive(unittest.TestCase):

    def test_multiple_elements(self):
        self.assertEqual(sum_of_list([1, 2, 3, 4, 5]), 15)


if __name__ == '__main__':
    unittest.main()