import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname( os.path.dirname(__file__)))
sys.path.append(os.path.dirname( os.path.dirname(os.path.dirname(__file__))))
from  numerical_analysis.polynome.polynome import *
from numerical_analysis.interpolation.lagrange import initialize
n=0
vals={}
xiList=[]
def initialize(newN, xiYi:dict):
    global n, vals,xiList
    n=newN
    vals=xiYi
    xiList=list(vals.keys())

def dividedDifference(arr):
    # arr represnets an array 
    if len(arr)==1:
        return vals[arr[0]]

    if len(arr)<=2:
        #vals[arr[0]] represnete represente la f(arr (0+))
        return (vals[arr[0]] - vals[arr[1]])/ (arr[0] - arr[1])
    else:
        return (dividedDifference(arr[:-1])-dividedDifference(arr[1:]) )/(arr[0]-arr[-1])

def interpolationNewton(n, xiYi):
    initialize(n, xiYi)
    dividedDifferenceList=[]
    polynomsArr=[Polynome(0,[1])]
    for i in range(1,n+1):
        dividedDifferenceList.append(dividedDifference(xiList[:i]))
    for i in range(1,n):
        polynomProd=Polynome.productOfTwoPolynoms(polynomsArr[i-1], Polynome(1,[-xiList[i-1],1]))
        polynomsArr.append(polynomProd)
    
    for k,v in enumerate(polynomsArr):
        v.productWithConstant(dividedDifferenceList[k])
    
    polynom=Polynome.sumOfPolynoms(polynomsArr)

    #print
    print("\n\nNEWTON: ", end="")
    Polynome.printPolynom(polynom.coeffs.values())
    return polynom
