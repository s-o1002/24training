import sys
import problem1
import unittest
from io import StringIO

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    # 真ん中に挿入
    def test_insert_middle(self):
        x = [1, 2, 3, 4, 5]
        problem1.insert_value(x, 1, 100)

        expected_output = "[1, 2, 100, 3, 4, 5]"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # 先頭に挿入
    def test_insert_start(self):
        x = [1, 2, 3]
        problem1.insert_value(x, 0, 100)

        expected_output = "[1, 100, 2, 3]"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # 末尾に挿入
    def test_insert_end(self):
        x = [1, 2, 3]
        problem1.insert_value(x, 2, 100)

        expected_output = "[1, 2, 3, 100]"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # リストの範囲外の位置に挿入
    def test_index_out_of_range(self):
        x = [1, 2, 3]
        with self.assertRaises(IndexError):
            problem1.insert_value(x, 3, 100)

if __name__ == '__main__':
    unittest.main()
