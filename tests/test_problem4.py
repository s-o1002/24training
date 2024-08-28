import sys
import problem4
import unittest
from io import StringIO

class TestProblem4(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    # 存在するものと存在しないものを1つずつ追加
    def test_add_dict_normal_case(self):
        problem4.add_dict({'apple': 10, 'grape': 20, 'orange': 30}, 'apple', 'pineapple')

        expected_output = "{'apple': 10, 'grape': 20, 'orange': 30, 'pineapple': -1}"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # 存在しないものだけ追加
    def test_add_dict_only_nonexistent(self):
        problem4.add_dict({'apple': 10, 'grape': 20, 'orange': 30}, 'pineapple', 'banana')

        expected_output = "{'apple': 10, 'grape': 20, 'orange': 30, 'pineapple': -1, 'banana': -1}"
        self.assertEqual(self.io.getvalue().strip(), expected_output)

    # 存在するものだけ追加
    def test_add_dict_only_existent(self):
        problem4.add_dict({'apple': 10, 'grape': 20, 'orange': 30}, 'apple', 'orange')

        expected_output = "{'apple': 10, 'grape': 20, 'orange': 30}"
        self.assertEqual(self.io.getvalue().strip(), expected_output)
    
    # 辞書が空の場合
    def test_add_dict_empty_dict(self):
        problem4.add_dict({}, 'apple', 'orange')

        expected_output = "{'apple': -1, 'orange': -1}"
        self.assertEqual(self.io.getvalue().strip(), expected_output)
    
    # 引数が辞書でない場合
    def test_add_dict_invalid_type(self):
        with self.assertRaises(TypeError):
            problem4.add_dict("banana", 'apple', 'orange')

if __name__ == '__main__':
    unittest.main()