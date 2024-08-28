import sys
import problem3
import unittest
from io import StringIO

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    # リストの長さが5の場合
    def test_print_even_index_normal_case(self):
        test_list = [1, 2, 3, 4, 5]
        problem3.print_even_index(test_list)

        expected_output = "1\n3\n5"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # リストが1つの要素しかない場合
    def test_print_even_index_single_element(self):
        test_list = [1]
        problem3.print_even_index(test_list)

        expected_output = "1"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # リストが空の場合
    def test_print_even_index_empty_list(self):
        test_list = []
        problem3.print_even_index(test_list)

        expected_output = ""
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # リストの長さが2の場合
    def test_print_even_index_multiple_elements(self):
        test_list = [10, 20, 30, 40, 50, 60]
        problem3.print_even_index(test_list)

        expected_output = "10\n30\n50"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # 引数がリストでない場合
    def test_print_even_index_invalid_type(self):
        with self.assertRaises(TypeError):
            problem3.print_even_index("not a list")

if __name__ == '__main__':
    unittest.main()
