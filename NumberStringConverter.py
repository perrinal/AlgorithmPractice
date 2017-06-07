# class to split the number of a string and translate in a string
class NumberStringConverter:
    
    
    def __init__(self , number):
        self.processingstack = list() #we use a stack to pop unfinished lists
        self.processingstack.append([list(),list(number)]) # the processing stack is a list of [temporary solution , numbers left to process]
        self.possibilities = list() # once we are a the end of the processing stack, we move the solution in there.
        self.charMap = list("abcdefghijklmnopqrstuvwxyz") #the index+1 gives the map to the number.
        
    def numberConverter(self):
        for possibility in self.possibilities:
            solution = ""
            for number in possibility:
                solution = solution + self.charMap[int(number) - 1]
            print (solution)
    
    def splitter(self):
        while len(self.processingstack) > 0: # we go through the processing stack while there are item
            #print (self.processingstack) #uncomment to see the processing stack evolving
            myitem = self.processingstack.pop(0)
            tmp_soltution1 = list(myitem[0]) #solution with 1 number
            tmp_soltution2 = list(myitem[0]) #solution with 2 numbers
            tmp_list1 = list(myitem[1]) #list to take 1 number
            tmp_list2 = list(myitem[1]) #list to take 2 numbers

            
            if len(tmp_list2) >1: # first we explore the solution tree with 2 numbers
                number1 = tmp_list2.pop(0)
                number2 = tmp_list2.pop(0)
                if int(number1+number2) < 26:
                    tmp_soltution2.append(number1+number2) 
                    self.processingstack.append([list(tmp_soltution2) , list(tmp_list2)]) #we do not have a solution yet but we put is back on the stack
            if len(tmp_list1) >0: # then explore with 1 number
                tmp_soltution1.append(tmp_list1.pop(0))
                self.processingstack.append([list(tmp_soltution1) , list(tmp_list1)]) #we do not have a solution yet but we put is back on the stack
            else: #no number on the right or the processing stack item so we have finished this item
                self.possibilities.append(myitem[0])
                                     
        

        
            


nsc = NumberStringConverter("112233")
nsc.splitter()
nsc.numberConverter()

                        
            
        
        
    
                
            
        
