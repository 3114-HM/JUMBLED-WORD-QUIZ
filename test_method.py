import unittest   # The test framework
import Options

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    def test_decrement(self):
        self.assertEqual(4, 4)
    
    def test_add(self):
        self.assertEqual(5+5,10)

if __name__ == '__main__':
    unittest.main()