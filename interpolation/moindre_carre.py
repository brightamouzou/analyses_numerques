from copy import copy
import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname( os.path.dirname(__file__)))
sys.path.append(os.path.dirname( os.path.dirname(os.path.dirname(__file__))))

print(sys.path)
from numerical_analysis.polynome.polynome import Polynome
from numerical_analysis.equations_lineaires.gauss import *
from numerical_analysis.equations_lineaires.utils import *

a=Polynome(2, [1,2,5])

Polynome.printPolynom(a.coeffs.values())
P=[]; B=[]
p=4; n=0
vals={-1:1, 2:5, 3:2, 7:8, 9:0}
xiList=list(vals.keys())
yiList=list(vals.values())

def initialize(newN, xiYi:dict):
    global n, vals,xiList, yiList
    #Avec moindre carres , n represnete le nombre de couple de points moins 1
    # n=newN-1
    n=newN
    vals=xiYi
    xiList=list(vals.keys())
    yiList=list(vals.values())
    for i in range(p+1):
        # exp=2*p-i
        B.append(sum([pow(xiList[q],p-i)*yiList[q] for q in range(n+1)]))
        P.append([ sum( [pow(xiList[j], 2*p-(q+i))  for j in range(n+1)] ) for q in range(p+1)])
        

def moindreCarres(n, xiYi):
    initialize(n, xiYi)
    newP=extendMatrixItems(P, B)
    Alpha=gauss(newP, len(newP))
    #print
    print("\n\nMOINDRE CARRES: ")
    Polynome.printPolynom((reversed(list(Alpha.values()))))


if __name__=="__main__":
    n=4
    vals={-1:1, 2:5, 3:2, 7:8, 9:0}
    moindreCarres(n, vals)