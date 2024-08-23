import sys
import problem7
import unittest
from io import StringIO

class TestProblem7(unittest.TestCase):
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_problem7_output(self):
        problem7.main()

        # 期待される出力
        expected_output = "[{'a': 6, 'b': 7, 'c': 6}, {'a': 1, 'b': 5, 'c': 8}, {'a': 4, 'b': 2, 'c': 3}]"

        # 出力が期待されるものであるか確認
        self.assertEqual(self.io.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()