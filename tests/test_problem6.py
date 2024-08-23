import sys
import problem6
import unittest
from io import StringIO

class TestProblem6(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_problem6_output(self):
        problem6.main()

        # 期待される出力
        expected_output = "[1, 2, 3, 4, 5]"

        # 出力が期待されるものであるか確認
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()