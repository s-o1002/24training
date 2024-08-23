import sys
import problem9
import unittest
from io import StringIO

class TestProblem9(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_problem1_output(self):
        problem9.main()

        # 期待される出力
        expected_output = "38"

        # 出力が期待されるものであるか確認
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()