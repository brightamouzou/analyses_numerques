from utils import derivee 


def fixedPoints(g, x0, epsilon=10e-10, nbItMax=100):
    try:
        if abs( derivee(g,x0) ) >1:
            return f"Cette methode ne converge pas car |g'({x0})|= {abs(derivee(g,x0))} > 1 . Essayez de changer x0"
        xn=x0
        xnPlus1=g(xn)
        i=0  #compteur
        while not limitReached(xn, xn+1, epsilon) and i<nbItMax:
            xn=xnPlus1
            xnPlus1=g(xn)
            i+=1
        
        if not limitReached(xn, xnPlus1, epsilon):
            return f"Cette methode ne converge pas au bout du nombre maximal diterations. Essayez de changer x0"
          
    except ZeroDivisionError:
        message=f"Division par 0 impossible: {xn} n'appartient pas à l'ensemble de definition"
        return message
    except:
        message="Aucune solution trouvée"
        return message
    else:
        return xnPlus1

def limitReached(xn, xnPlus1,epsilon=10e-10):
    return abs(xnPlus1 - xn)/abs(xnPlus1) < epsilon


if __name__=="__main__":
    print(fixedPoints(g,2.1))
    