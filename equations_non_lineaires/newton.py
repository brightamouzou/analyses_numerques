from cmath import exp
from cupshelpers import Printer
from utils import derivee

def newton(f, x0, epsilon=10e-10, nbItMax=100):
    
    try:
        xn=x0
        xnPlus1=findXnPlus1(f,xn)
        i=0

        while not limitReached(xn, xnPlus1,epsilon) and i<nbItMax and abs(f(xnPlus1))>=epsilon:
            xn=xnPlus1
            xnPlus1=findXnPlus1(f,xn)
            i+=1
    except ZeroDivisionError:
        message=f"Division par 0 impossible: {xn} n'appartient pas à l'ensemble de definition"
        return message
    except:
        message="Aucune solution trouvée"
        return message
    else:
        return xnPlus1


def findXnPlus1(f,xn):
    return xn - f(xn)/derivee(f, xn)

def limitReached(xn, xnPlus1,epsilon=10e-10):
    return abs(xnPlus1 - xn)/abs(xnPlus1) <= epsilon

if __name__=="__main__":
    print(newton(f, 0))