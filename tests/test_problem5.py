import sys
import problem5
import unittest
from io import StringIO

class TestPrintSlice(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    # 正常系
    def test_print_slice_normal_case(self):
        problem5.print_slice("training", 1, 4)
        expected_output = "rain"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # 空の文字列を渡す
    def test_print_slice_invalid_string_type(self):
        with self.assertRaises(ValueError):
            problem5.print_slice(123, 1, 4)

    # 整数でないx, yを渡す
    def test_print_slice_invalid_index_type(self):
        with self.assertRaises(ValueError):
            problem5.print_slice("training", "1", 4)

        with self.assertRaises(ValueError):
            problem5.print_slice("training", 1, "4")

    # xが負の値、yが文字列の長さを超える
    def test_print_slice_out_of_range(self):
        with self.assertRaises(ValueError):
            problem5.print_slice("training", -1, 4)

        with self.assertRaises(ValueError):
            problem5.print_slice("training", 1, 10)

    # 文字列全体を切り取る
    def test_print_slice_edge_case(self):
        problem5.print_slice("training", 0, 7)
        expected_output = "training"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
