## Jocelyn Huang
## 01/13/2014
## A Plethora of Weighting Methods
import math

def sigmoid(value):     # Inspired by sigmoid function. 10/(1+e^(.1|x-50|)) Somewhat of a sharp downwards curve :I
    if(value <= 0 or value >= 100): return 1
    newVal = math.ceil(10.0/(1 + math.pow(math.e, 0.1*math.fabs(value-50))))
    return newVal
    
def testWeighting(value):
    return value+1