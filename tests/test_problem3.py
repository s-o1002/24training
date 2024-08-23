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

    def test_problem3_output(self):
        problem3.main()

        # 期待される出力
        expected_output = "1\n3\n5"

        # 出力が期待されるものであるか確認
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()