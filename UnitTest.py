from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = { 1: ("abcde", "cdeab", True), 2: ("abcde", "abced", False) } 
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, goal, output = self.__testCases[1]
        result = self.__obj.rotateString(s = s, goal = goal)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)


    @timeout(0.5)
    def test_Case2(self):
        s, goal, output = self.__testCases[2]
        result = self.__obj.rotateString(s = s, goal = goal)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()