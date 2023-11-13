import unittest
import calc


# By inheriting from unittest.TestCase,
# it gains all the methods and capabilities needed to act as a test case for Python's unittest module
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
# In Python, you can use two general approaches to deal with resource management. You can wrap your code in:
#   A try … finally construct
#   A with construct
# The first approach is quite general and allows you to provide setup and teardown code to manage any kind of resource. However, it’s a little bit verbose. Also, what if you forget any cleanup actions?
# The Python with statement creates a runtime context that allows you to run a group of statements under the control of a context manager
if __name__ == '__main__':
    unittest.main()
# In summary, the if __name__ == "__main__": statement is a useful way to ensure that code is only executed when a
# Python script is run as a standalone program, and not when it is imported as a module.
