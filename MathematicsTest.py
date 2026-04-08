import unittest
from Mathematics import Mathematics
import random

class MathematicsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mIns = Mathematics()

    def setUp(self):
        self.first_num = random.randint(1, 100)
        self.second_num = random.randint(1, 100)
        self.expected_sum = self.first_num + self.second_num
        self.expected_mul = self.first_num * self.second_num

    def test_can_add(self):
        actual_sum = self.mIns.addition(self.first_num, self.second_num)
        self.assertEqual(actual_sum, self.expected_sum)

    def test_can_multiply(self):
        actual_value = self.mIns.multiplication(self.first_num, self.second_num)
        self.assertEqual(actual_value, self.expected_mul)

if __name__ == "__main__":
    unittest.main()