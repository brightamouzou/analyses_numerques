from math import sqrt
from lu import LYEqualsToB,UXEqualsToY
from copy import deepcopy

def handleRadicandeLessThanZero(diff):
    if diff<0: 
        print("Imossible: Le radicande doit etre superieur à 0")
        exit()

 
def choleskyFactorisation(A):
    n = len(A)

    L = [[0.0] * n for i in range(n)]
    
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k):
                handleRadicandeLessThanZero(A[i][i]-tmp_sum)
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                try:
                    L[i][k] = (1/ L[k][k] * (A[i][k] - tmp_sum))
                except ZeroDivisionError:
                    print(f"\n\nCHOLESKY: Impossible car  la matrice A n'est pas symetrique et definie definie positive")
                    exit()
    return L


def cholesky(a,b):

    if isSymetric(a):
        l=choleskyFactorisation(a)
        transpoL=[list(i) for i in zip(*deepcopy(l))]
        y=LYEqualsToB(l,b)
        x=UXEqualsToY(transpoL, list(y.values()))

        for v in x:
            if abs(x[v])<10e-10:
                x[v]=0
                
        return x
    else:
        return "La matrice A n'est pas symetrique ou definie positive, par consequent cette methode ne fournit pas de soultions"


# A=[[1,1,1,1],[1,5,5,5],[1,5,14,14],[1,5,14,15]]
# b=[1,4,8,8]
# cholesky(A,b)

def isSymetric(a:list):
    isSymetric=False
    n=len(a)
    for i in range(len(a)):
        for j in range(i+1,n):
            if (a[j][i]!=a[i][j]):
                return isSymetric
                break
    isSymetric=True
    return isSymetric
