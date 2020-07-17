import unittest
from addition import addition


class TestAdditionMethods(unittest.TestCase):
    def test_2and2equals4(self):
        self.assertEqual(addition(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
