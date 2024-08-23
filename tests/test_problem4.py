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

    def test_problem1_output(self):
        problem4.main()

        # 期待される出力
        expected_output = "{'apple': 10, 'grape': 20, 'orange': 30, 'pineapple': -1}"

        # 出力が期待されるものであるか確認
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()