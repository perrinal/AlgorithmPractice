# Comparing 2 fibonacci serie algorithm to find the Nth number
# 1 uses a normal loop to reach the Nth number with O(n)
# 2 uses a maths shortcut of the fibonacci serie with O(log n)

from datetime import datetime
from decimal import Decimal

def fib(n):
    fibn0 = 0;
    fibn1 = 1;
    for i in range(0,n-1):
       fibtmp = fibn1
       fibn1 = fibn0 + fibn1
       fibn0 = fibtmp
    return fibn1


# f(n)^2 + f(n+1)^2 = f(2n + 1) for uneven numbers
# f(n+1)^2 + f(n-1)^2 = f(2n) for even numbers
def fasterfib(n):
    halfn = n//2
    #print (halfn)
    rest = n%2

    fibn0 = 0;
    fibn1 = 1;
    for i in range(0,halfn):
       fibtmp = fibn1
       fibnm1 = fibn0
       fibn1 = fibn0 + fibn1
       fibn0 = fibtmp
        
    #print (fibnm1)
    #print (pow(fibnm1,2)) 
    #print (fibn0)
    #print (pow(fibn0,2)) 
    #print (fibn1)
    #print (pow(fibn1,2))

    if (rest == 1):
        return pow(fibn0,2) + pow(fibn1,2)
    else:
        return pow(fibn1,2) - pow(fibnm1,2)

def testFunction(functionName, Number):
    start = datetime.now()
    # Display 
    print("{:.2E}".format(Decimal(functionName(Number))))
    print (datetime.now() - start)

    
Number = 300000
testFunction(fib, Number)
testFunction(fasterfib, Number)
        
        
