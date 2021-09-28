import unittest
from basic import myStack

class TestStack(unittest.TestCase):
    def test_push_single(self):
        test_stack = myStack()
        test_stack.push(2)
        self.assertEqual(test_stack.items, [2])

    def test_push_multiple(self):
        test_stack = myStack()
        test_stack.push(2)
        test_stack.push(3)
        test_stack.push(4)
        self.assertEqual(test_stack.items, [2,3,4])

    def test_pop_single(self):
        test_stack = myStack()
        test_stack.push(2)
        popped = test_stack.pop()
        self.assertEqual(popped, 2)

    def test_pop_multiple(self):
        test_stack = myStack()
        test_stack.push(2)
        test_stack.push(3)
        test_stack.push(4)
        test_stack.pop()
        self.assertEqual(test_stack.items, [2,3])

if __name__ == '__main__':
    unittest.main()
