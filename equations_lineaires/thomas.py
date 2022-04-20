# def thomas(a):
import sys
from gauss import gauss
from utils import extendMatrixItems


def isTriDiagonalMatrix(mat:list):
    l=len(mat)
    mil=l/2
    milPrime=mil

    for i in range(l):
        for j in range(l):
            
            if(i<=mil):
                if j>=milPrime:
                    if mat[i][j]!=0: return False
        milPrime+=1         
    return True

def elimination(a:list):
    n=len(a)
    for i in range(len(a)):
        a[i][i+1]=0

def thomas(a,b):
    if isTriDiagonalMatrix(a):
        newA=extendMatrixItems(a,b)
        return gauss(newA, len(a))
    else:
        return "La matrice A n'est pas tridiagonale , donc cette methode ne fournit aucune solution"

if __name__=='__main__':
    sys.stdin=open("luMat.txt", "r")
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
    # print(f"Veuillez saisir les éléments de la colonne {j+1} separés par des espaces")
        a.append([int(k) for k in input(f"Colonne {i+1}:").split()])
    print(a)
    print(isTriDiagonalMatrix(a))