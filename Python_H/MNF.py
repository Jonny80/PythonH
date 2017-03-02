import math


def MNF(a, b, c):
    e1 = (b-math.sqrt(b*b-(4*a*c)))/2*a
    e2 = (b+math.sqrt(b*b-(4*a*c)))/2*a
    print(e1,e2)

MNF(1,2,2)

