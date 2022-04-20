from cmath import exp
from utils import derivee
# f=lambda x: x**3 - 5*x**2 + 7*x -3

def secante(f, x0,x1, epsilon=10e-10, nbItMax=100):
    
    try:
        xnMoins1=x0
        xn=x1
        xnPlus1=findXnPlus1(f,xnMoins1, xn)
        i=0

        while not limitReached(xnMoins1,xn, epsilon) and i<nbItMax and abs(f(xnPlus1))>=epsilon:
            xnMoins1=xn
            xn=xnPlus1
            xnPlus1=findXnPlus1(f,xnMoins1, xn)
            i+=1
    except ZeroDivisionError:
        message=f"Division par 0 impossible: {xn} n'appartient pas à l'ensemble de definition"
        return message
    except:
        message="Aucune solution trouvée"
        return message
    else:
        return xnPlus1


def findXnPlus1(f,xnMoins1,xn):
    return xn - (f(xn)*(xn - xnMoins1))/(f(xn) - f(xnMoins1))

def limitReached(xn, xnPlus1,epsilon=10e-9):
    return abs(xnPlus1 - xn)/abs(xnPlus1) < epsilon

if __name__=="__main__":
    print(secante(f, 0,1))