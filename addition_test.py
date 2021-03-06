import unittest
from addition import addition


class TestAdditionMethods(unittest.TestCase):
    def test_2and2equals4(self):
        self.assertEqual(addition(2, 2), 4)

    def test_2and2and2equals6(self):
        self.assertEqual(addition(2, 2, 2), 6)

    def test_emptySumEquals0(self):
        self.assertEqual(addition(), 0)

    def test_exceedMaxInt(self):
        # Max int is 2147483647, but when its larger than that is converted to negative value by subtracting 4294967296
        # So There is no limit for long integer literals apart from what can be stored in available memory.
        self.assertEqual(addition(4294967296, 4294967296), 8589934592)

    def test_2010and2010Equals4020(self):
        self.assertEqual(addition(2010, 2010), 4020)

    def test_2andMinus200EqualsMinus198(self):
        self.assertEqual(addition(2, -200), -198)

    def test_sendListOfarguments(self):
        self.assertEqual(addition(nums=[2, 2]), 4)

    def test_200and200NotEquals1(self):
        self.assertNotEqual(addition(200, 200), 1)

    def test_2200and2200NotEquals4(self):
        self.assertNotEqual(addition(2200, 2200), 4)

    def test_2and2NotEquals5(self):
        self.assertNotEqual(addition(2, 2), 5)

    def test_14and12NotEquals24(self):
        self.assertNotEqual(addition(14, 14), 24)

    def test_raisesInvalidType(self):
        with self.assertRaises(TypeError):
            addition("a", "b")


if __name__ == '__main__':
    unittest.main()
