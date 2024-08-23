import sys
import problem2
import unittest
from io import StringIO

class TestMakeTuple(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    # リストの最初と最後の要素をタプルに変換
    def test_make_tuple_normal_case(self):
        test_list = [1, 2, 3, 4, 5]
        problem2.make_tuple(test_list)

        expected_output = "(1, 5)"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # リストが1つの要素しかない場合
    def test_make_tuple_single_element(self):
        test_list = [1]
        with self.assertRaises(IndexError):
            problem2.make_tuple(test_list)

    # リストが空の場合
    def test_make_tuple_empty_list(self):
        test_list = []
        with self.assertRaises(IndexError):
            problem2.make_tuple(test_list)

    # リストが2つの要素しかない場合
    def test_make_tuple_two_elements(self):
        test_list = [1, 2]
        problem2.make_tuple(test_list)

        expected_output = "(1, 2)"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
