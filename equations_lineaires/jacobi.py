from copy import deepcopy
import math
from utils import permuationMatrix, permuationVector


b=[]
a=[]
n=0

def initializeAandBJacobi(newA, newB, newN):
    global n, a,b
    #Vauleur de la variable globale n changée avec newN
    n=newN

    #Mettre a jour les valuers de a et b avec de vrais donnees passees en paramètre
    a=deepcopy(newA)
    b=deepcopy(newB)


def findXPlus1Jacobi(xk, i):

    if(a[i][i]==0):
        permuationMatrix(a,i,b)

    return (b[i]-sum([a[i][j]*xk[j] for j in range(n) if j!=i]) )/a[i][i]

def differenceOfVectors(vectA,vectB):
    diff=[]
    for i in range(len(vectB)):
        diff.append(vectB[i]-vectA[i])
    return diff

def normVector(vect):
    return math.sqrt(sum([i**2 for i in vect]))


def limitReached(xk:list,xkPlus1:list, eps):
    dif=differenceOfVectors(xk, xkPlus1)
    normXkPlus1=normVector(xkPlus1)

    # print("norme",normVector(dif)/normVector(xkPlus1) )

    if normXkPlus1==0:
        raise ValueError("La norme de xk+1 est égale à 0:Division par zero impossible ")
 
    return normVector(dif)/normVector(xkPlus1)<eps



def jacobiIteration(xk):
    #return [findXPlus1Jacobi(xk) for i in range(n)]
    for i in range(n):
        xk[i]=findXPlus1Jacobi(xk, i)    
    
    return xk


def jacobi(X0:list, eps, nbItMax=100):

    if isDiagonaleDominante(a):
        xk=X0
        xkPlus1=[]
        for i in range(n):
            xkPlus1.append(findXPlus1Jacobi(xk,i))
        
        compt=0    

        # return solutions
        while not limitReached(xk, xkPlus1,eps) and compt<=nbItMax:
            xk=jacobiIteration(xk)
            xkPlus1=[findXPlus1Jacobi(xk,i) for i in range(n)]
            compt+=1

        # print(f"JACOBI y est arrivé au bout de {compt} iterations")

        #x0 est le vecteur  x de base pour les iterations
        solutions=dict()
        for k,v in enumerate(xk):
            solutions.__setitem__(f"x{k+1}",v)

        return solutions
    else:
        return "La matrice A n'est pas à diagonale dominante , par consequent cette methode ne fournit pas de solutions"


def isDiagonaleDominante(mat):
    cmpt=0    
    for i in range(n):
        cmpt+=int(abs(a[i][i]) >= sum([abs(j) for j in mat[i] if j!=mat[i][i]]))
    return cmpt>=len(mat)

        

