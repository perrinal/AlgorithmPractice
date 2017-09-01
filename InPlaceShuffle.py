from random import randint

class InPlaceShuffle:  
    def __init__(self):
        self.MyArray = list(range(0,52)) #52 cards
        
    def Shuffle(self):
        # The idea is to pop a random element and then insert it at the begining of the array.
        # The cursor goes towards the end of the array so what have been already suffled is not shuffled again.
        for i in range(0,len(self.MyArray)-1):
            tmpPos = randint(i, len(self.MyArray)-1)
            tmpItem = self.MyArray.pop(tmpPos)
            self.MyArray.insert(0,tmpItem)


myIPS = InPlaceShuffle()
print (myIPS.MyArray)
myIPS.Shuffle()
print (myIPS.MyArray)                            
                                
    
