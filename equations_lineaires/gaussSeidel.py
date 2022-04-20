from jacobi import *
b=[]
a=[]
n=0

def initializeAandBGaussSeidel(newA, newB, newN):
    global n, a,b
    #Vauleur de la variable globale n changée avec newN
    n=newN

    #Mettre a jour les valuers de a et b avec de vrais donnees passees en paramètre
    a=deepcopy(newA)
    b=deepcopy(newB)

def findXPlus1GaussSeidel(xk, i):


    tmp=b[i]-sum([a[i][j]*xk[j] for j in range(i+1,n) if j!=i])- sum([a[i][j]*findXPlus1GaussSeidel(xk, j) for j in range(i)])
    return tmp/a[i][i]


def jacobiIteration(xk):
    for i in range(n):
        xk[i]=findXPlus1GaussSeidel(xk, i)    
    
    return xk


def gaussSeidel(X0:list, eps, nbItMax=100):

    if isDiagonaleDominante(a):

        
        xk=X0
        xkPlus1=[]
        for i in range(n):
            xkPlus1.append(findXPlus1GaussSeidel(xk,i))
        
        compt=0    

        # return solutions
        while not limitReached(xk, xkPlus1,eps) and compt<=nbItMax:
            xk=jacobiIteration(xk)
            xkPlus1=[findXPlus1GaussSeidel(xk,i) for i in range(n)]
            compt+=1

        # print(f"GAUSS-SEIDEL y est arrivé au bout de {compt} iterations")

        
        #x0 est le vecteur  x de base pour les iterations
        solutions=dict()
        for k,v in enumerate(xk):
            solutions.__setitem__(f"x{k+1}",v)

        return solutions
    else:

        return "La matrice A n'est pas à diagonale dominante , par consequent cette methode ne fournit aucune solutions"


