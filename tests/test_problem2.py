import sys
import problem2
import unittest
from io import StringIO

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_problem1_output(self):
        problem2.main()

        # 期待される出力
        expected_output = "(1, 5)"

        # 出力が期待されるものであるか確認
        self.assertEqual(self.captor.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()