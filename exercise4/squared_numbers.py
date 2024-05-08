# כתוב פונקציה המקבלת רשימה של מספרים ומחזירה רשימה חדשה עם ריבוע הערכים
# מהרשימה המקורית
def squared_numbers(numbers):
    n = []
    for i in numbers:
        n.append(i**2)
    return n

# ================================================
#                   UNITTEST AREA
# ================================================
import unittest

class TestSquaredNumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(squared_numbers([]), [])

    def test_positive_numbers(self):
        self.assertEqual(squared_numbers([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()