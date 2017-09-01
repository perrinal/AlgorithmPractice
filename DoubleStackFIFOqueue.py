# Exercise: Implement a queue with 2 stacks. 
#Your queue should have an enqueue and a dequeue 
#function and it should be "first in first out" (FIFO). 


#Designed Algorithm:
#On enqueue we push on the ThePopStack if there is no element until there is 1 then on the second stack
#On dequeue if ThePopStack is empty we push in it all the element from the push stack which put them in LIFO order
import unittest

class DoubleStackFIFOqueue:
    
    def __init__(self):
        self.ThePopStack = []
        self.ThePushStack = []     

    def __str__(self):
        return "Pop Stack  : " + str(self.ThePopStack) + "\n"\
               "Push Stack : " + str(self.ThePushStack)

    def enqueue(self, Obj):
        if not self.ThePopStack:
            self.ThePopStack.append(Obj)
        else:
            self.ThePushStack.append(Obj)

    def dequeue(self):
        if not self.ThePopStack:
            raise IndexError ("Queue is Empty")
        else:
            TopOfThePop = self.ThePopStack.pop()
            if not self.ThePopStack:
                self.transferStacks()
            return TopOfThePop

    def transferStacks(self):
        while self.ThePushStack:
            self.ThePopStack.append(self.ThePushStack.pop())



class TestDoubleStackFIFOqueue(unittest.TestCase):

    def setUp(self):
        self.DSFQ = DoubleStackFIFOqueue()

    def test_enqueue(self):
        self.DSFQ.enqueue("A")
        self.assertEqual(self.DSFQ.ThePopStack[0], "A",'Pop Stack expected value A')
        
    def test_dequeue(self):
        self.DSFQ.enqueue("A")
        Val = self.DSFQ.dequeue()
        self.assertEqual(Val, "A",'expected value A')

    def test_dequeueEmpty(self):    
        self.assertRaises(IndexError, self.DSFQ.dequeue)

    def test_ManyEnqueue(self):
        self.DSFQ.enqueue("A")
        self.DSFQ.enqueue("B")
        self.DSFQ.enqueue("C")
        self.DSFQ.enqueue("D")
        self.assertEqual(self.DSFQ.ThePopStack[0], "A",'Pop Stack expected value A')
        self.assertEqual(self.DSFQ.ThePushStack[0], "B",'Push Stack expected value B')
        self.assertEqual(self.DSFQ.ThePushStack[1], "C",'Push Stack expected value C')
        self.assertEqual(self.DSFQ.ThePushStack[2], "D",'Push Stack expected value D')

    def test_ManyEnqueueDequeue(self):
        self.DSFQ.enqueue("A")
        self.DSFQ.enqueue("B")
        self.DSFQ.enqueue("C")
        self.DSFQ.enqueue("D")
        TestList = []
        TestList.append(self.DSFQ.dequeue())
        TestList.append(self.DSFQ.dequeue())
        TestList.append(self.DSFQ.dequeue())
        TestList.append(self.DSFQ.dequeue())
        self.assertEqual(TestList, ["A","B","C","D"],'expected value [A,B,C,D]')


    def test_MixEnqueueDequeue(self):
        TestList = []
        self.DSFQ.enqueue("A")
        self.DSFQ.enqueue("B")
        TestList.append(self.DSFQ.dequeue())
        self.DSFQ.enqueue("C")
        self.DSFQ.enqueue("D")
        self.DSFQ.enqueue("E")
        TestList.append(self.DSFQ.dequeue())
        TestList.append(self.DSFQ.dequeue())   
        self.DSFQ.enqueue("F")
        TestList.append(self.DSFQ.dequeue())
        TestList.append(self.DSFQ.dequeue())
        
        TestList.append(self.DSFQ.dequeue())
        print("Dequeue\n" + str(TestList) +"\n"+str(self.DSFQ))
        self.assertEqual(TestList, ["A","B","C","D","E","F"],'expected value [A,B,C,D,E,F]')
  
        
if __name__ == '__main__':
    unittest.main()
