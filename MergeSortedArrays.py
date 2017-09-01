
import unittest
from heapq import merge

def merge_lists(list1, list2):
    #Function that runs in O(n) doing only one pass of each list in input
    #It also saves space by poping the elements from the original lists.
    mergedList = list()
    while len(list1)>0 or len(list2)>0:
        #Manage the lists are empty
        if len(list1) == 0: 
            mergedList.append(list2.pop(0))
        elif len(list2) == 0:
            mergedList.append(list1.pop(0))
        else: # does the merge comparison
            if list1[0] > list2[0]:
                mergedList.append(list2.pop(0))
            else:
                mergedList.append(list1.pop(0))
    return mergedList
        

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print (list(merge(my_list , alices_list))) #this one is built in, and does not empty the original lists
print (merge_lists(my_list, alices_list))


# Unit testing example for the above function
class TestMergeSortedArray(unittest.TestCase):

    def test_merge_lists(self):
        self.assertEqual(merge_lists([3, 4, 6, 10, 11, 15],[1, 5, 8, 12, 14, 19]),\
                         [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])
    def test_merge_lists_Empty(self):
        self.assertEqual(merge_lists([],[]),\
                         [])
    def test_merge_lists_Empty1(self):
        self.assertEqual(merge_lists([1,2,3],[]),\
                         [1,2,3])
    def test_merge_lists_Same(self):
        self.assertEqual(merge_lists([0,0],[0,0]),\
                         [0,0,0,0])


if __name__ == '__main__':
    unittest.main()
