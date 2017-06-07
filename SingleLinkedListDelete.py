class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

    def printNode(self):
        #print the chain from Node
        print (self.value, end="")
        if (self.next != None):
            print (" -> " , end="")
            self.next.printNode()

    def deleteNode(self):
        self.value = self.next.value
        self.next = self.next.next
        # O(1) solution
        #In-place operations like this can save time and/or space,
        #but they're risky as any pointer to the deleted node have new values.


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
f = LinkedListNode('F')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

a.printNode()
print()
c.deleteNode()
a.printNode()
