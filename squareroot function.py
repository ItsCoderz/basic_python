import math 
s=[4,9,16,25,64,100]

def square_function(s) :
    squareroot=[]
    square=[]
    for idx, x in enumerate(s):
        value = s [idx] * s[idx]
        square.append(value)
        squareroot.append(int(math.sqrt(s[idx])))
    print(squareroot)
    print(square)    
square_function(s)  
