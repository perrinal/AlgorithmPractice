import unittest

class RedBlackNode:

    def __init__(self , data = None, color=True):
        self.data = data
        self.left = None
        self.right = None
        self.color = bool(color) #will bt red|true or black|false (ieasier to use boolean than strings)

    def insertLeft (self, data):
        self.left = RedBlackNode (data, not self.color)
        
    def insertRight (self, data):
        self.right = RedBlackNode (data, not self.color)

    def insertData(self, data):
        if (self.data == None):
            self.data = data
            return True

        elif self.data > data:
            if self.left == None:
                self.insertLeft(data)
            else:
                self.left.insertData(data)
                
        elif self.data < data:
            if self.right == None:
                self.insertRight(data)
            else:
                self.right.insertData(data)

    def __str__(self):
        return str(self.data) + "{"+str(self.color)+"}" + "\n" +str(self.left) + " " +str(self.right) + "\n"
        

class RedBlackBinaryTree:
    def __init__(self):
        self.root = RedBlackNode();
    
    def getRoot(self):
        return self.root
    
    def insertData(self, data):
        self.root.insertData(data)

    def __str__(self):



    def printRedBlackBinaryTree(prefix, isTail):
        print (prefix + (isTail ? "└── " : "├── ") + name)
        for int i = 0; i < children.size() - 1; i++:
            
            children.get(i).print(prefix + (isTail ? "    " : "│   "), false);
        }
        if (children.size() > 0) {
            children.get(children.size() - 1)
                    .print(prefix + (isTail ?"    " : "│   "), true);

        



class TestRedBlackBinaryTree(unittest.TestCase):

    def setUp(self):
        self.RBBT = RedBlackBinaryTree()

    def test_RedBlackBinaryTree_Constructor(self):
        self.assertEqual(self.RBBT.root.data, None,'expected value None')

    def test_RedBlackBinaryTree_InsertData(self):
        self.RBBT.insertData(2)
        self.RBBT.insertData(1)
        self.RBBT.insertData(3)
        self.RBBT.insertData(4)
        print (self.RBBT)
        self.assertEqual(self.RBBT.root.data, 2,'expected value 2')
        self.assertEqual(self.RBBT.root.left.data, 1,'expected value 1')
        self.assertEqual(self.RBBT.root.right.data, 3,'expected value 3')




if __name__ == '__main__':
    unittest.main()
