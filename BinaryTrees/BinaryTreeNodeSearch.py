
import unittest
from heapq import merge

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

# Unit testing example for the above function
class TestBinaryTreeSearch(unittest.TestCase):

    def setUp(self):
        self.BTN = BinaryTreeNode(None)
        self.BT = BinaryTree()

    def test_BinaryTreeNode_insert_left(self):
        self.BTN.insert_left(1)
        self.assertEqual(self.BTN.left.value, 1,'expected value 1')
        
    def test_BinaryTreeNode_insert_right(self):
        self.BTN.insert_right(1)
        self.assertEqual(self.BTN.right.value, 1,'expected value 1')
        
    def test_BinaryTree_insert_left(self):
        self.assertEqual(self.BTN.right.value, 1,'expected value 1')
        


if __name__ == '__main__':
    unittest.main()
