import unittest

from selectStock import selectStock


class TestSelectionStock(unittest.TestCase):

    def test_base_case(self):
        saving = 250
        currentValue = [175, 133, 109, 210, 97]
        futureValue = [200, 125, 128, 228, 133]
        self.assertEqual(selectStock(saving, currentValue, futureValue), 55)

    def test_simple_case(self):
        saving = 30
        currentValue = [1, 2, 4, 6]
        futureValue = [5, 3, 5, 6]
        self.assertEqual(selectStock(saving, currentValue, futureValue), 6)

    def test_complex_case(self):
        saving = 938
        currentValue = [29, 192, 150, 91, 65, 147, 206, 211, 173, 250, 168, 231, 77, 65, 65, 195, 220, 63, 129, 4, 286,
                        162,204, 22, 20, 183, 69, 242, 58, 91, 3, 55, 228, 216, 141]
        futureValue = [247, 182, 76, 292, 263, 98, 287, 194, 285, 233, 6, 180, 165, 293, 273, 148, 251, 120, 114, 282, 198,
                       32, 135, 294, 279, 37, 55, 280, 252, 219, 84, 290, 65, 103, 168]
        self.assertEqual(selectStock(saving, currentValue, futureValue), 2757)
