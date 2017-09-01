from random import randint

class SingleRiffle:
    deck = []
    half1 = []
    half2 = []

    @staticmethod
    def getRandom(floor, ceilling ,limit = None):
        rdm = randint(floor,ceiling)
        if (rdm > limit and limit != None):
            return limit
        return rdm
    
    def __init__(self):
        # The init creates a single Riffle Deck

        split = randint(1,52)
        deck =[]
        for i in range (1,split):
            self.half1.append(i)
        for i in range (split + 1, 52):
            self.half2.append(i)

        tmpHalf1 = self.half1
        tmpHalf2 = self.half2

        while (len(tmpHalf1) > 0 and len (tmpHalf2) >0):
            self.deck.extend(self.getCard(tmpHalf1))
            self.deck.extend(self.getCard(tmpHalf2))

              
    def getCard(self, half):
        res = []
        for i in range(0,getRandom(0,6,len(half))):
            res.append(half.pop())
        return res
                             
    def __str__(self):
        return str(self.half1)+"\n"+str(self.half2)+"\n"+str(self.deck)+"\n"

  
        

    #def checkSingleRiffle(self)
#
 #       while (len(self.half1) > 0 and len(self

sr = SingleRiffle()
print(sr)
