from math import prod
import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname( os.path.dirname(__file__)))
sys.path.append(os.path.dirname( os.path.dirname(os.path.dirname(__file__))))
from numerical_analysis.polynome.polynome import *
n=0
vals={}

def initialize(newN, xiYi:dict):
    global n, vals
    n=newN
    vals=xiYi

def liOfX(i):
    xiList=list(vals.keys())
    polynomsArr=[]
    prodAtDenominateur=prod([xiList[i]-xiList[j] for j in range(n) if j!=i])
    for q in range(n):
        if(q!=i):
            polynomsArr.append(Polynome(1, [-xiList[q],1]))
    
    product=Polynome.productOfPolynoms(polynomsArr)
    product.coeffs=dict(map(lambda x:(x, product.coeffs[x]/prodAtDenominateur),product.coeffs))
    return product
    

def interpolationLagrange(n, xiYi:dict):
    initialize(n, xiYi)

    yiList=list(vals.values())
    polynomsArr=[]
    for i in range(n):
        polynom=liOfX(i)
        polynom.coeffs=dict(map(lambda x:(x, polynom.coeffs[x]*yiList[i]),polynom.coeffs))
        polynomsArr.append(polynom)
    sum=Polynome.sumOfPolynoms(polynomsArr)
    print("\n\nLAGRANGE: ",end="")
    Polynome.printPolynom(list(sum.coeffs.values()))

    return sum


if __name__=="__main__":
    print(interpolationLagrange())
