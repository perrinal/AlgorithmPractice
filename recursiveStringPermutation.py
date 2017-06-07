class recursiveStringPermutation:
    def __init__(self, string):
        self.string = string
        self.answerSet = set()
        self.recuStringPermut(list(self.string) , "")

    def recuStringPermut(self , data , currentString ):
        #print (data)
        #print (currentString)
        if len(data) == 0:
             self.answerSet.add(currentString);
             return True;
        for i in range(0,len(data)):
            self.recuStringPermut(data[0:i]+data[i+1:] , currentString + str(data[i]))
        
            
myRSP = recursiveStringPermutation("abcde")
print (myRSP.answerSet)
