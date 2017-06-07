class HanoiTowers:
    stacks = [[],[],[]]
    maxring = 0 

    def __init__(self, rings):
        self.maxring = rings
        for i in range (0,rings):
            self.stacks[0].append(rings-i)
        self.display()


    def display(self):
        for height in range(0, self.maxring):
            for stack in self.stacks:
                if height < len(stack):
                    sprintf = "%2d" % stack[height]
                    print(sprintf, end=" ")
                else:
                    print (" | ",end="")
            print () #add a \n
        print ()
            
    def moveTower(self, height,fromPole, toPole, withPole):
        if height >= 1:
            self.moveTower(height-1,fromPole,withPole,toPole)
            self.move(fromPole,toPole)
            self.moveTower(height-1,withPole,toPole,fromPole)       

    def move(self, source, dest):
        disk = self.stacks[source].pop()
        self.stacks[dest].append(disk)
        self.display()
            
        
myHT = HanoiTowers(5)
myHT.moveTower(myHT.maxring,0, 1, 2)

            
