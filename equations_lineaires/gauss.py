import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname( os.path.dirname(__file__)))
sys.path.append(os.path.dirname( os.path.dirname(os.path.dirname(__file__))))
from numerical_analysis.equations_lineaires.utils import permuationMatrix, supTrigonization

def xiFormul(line:list, lineNum:int, triangMatrix, n)->float:
    """
        formule generale: xi=( bi - sum(k alant de i+1 à n de aik*xk) )/aii
    """
    i=lineNum

    if line[i]==0:
        permuationMatrix(triangMatrix,i)

        # raise ValueError("La matrice A n'est pas inversible => Nombre de solutions : 0")
        
    if i==(n-1):#n-1 parce que nous travaillons sur les tableaux et la nième ligne devient la (n-1)ième ligne 
        return ( line[-1]/line[i])
    else:
        tmp=sum([line[k]*xiFormul(triangMatrix[k], k,triangMatrix,n) for k in range(i+1,n)]) # sum(k alant de i+1 à n de aik*xk)
        return ( line[-1] - tmp )/line[i]


def xiFormulWithSupMatrix(line:list, lineNum:int, triangMatrix, n)->float:
    """
        formule generale: xi=( bi - sum(k alant de 1 à i-1 de aik*xk) )/aii
    """

    i=lineNum

    if line[i]==0:
        raise ValueError("La matrice A n'est pas inversible => Nombre de solutions : 0")
        
    if i==(n-1):#n-1 parce que nous travaillons sur les tableaux et la nième ligne devient la (n-1)ième ligne 
        return ( line[-1]/line[i])
    else:
        tmp=sum([line[k]*xiFormul(triangMatrix[k], k,triangMatrix,n) for k in range(0,i-1)]) # sum(k alant de i+1 à n de aik*xk)
        return ( line[-1] - tmp )/line[i]


def gauss(arr:list, n:int)->dict:

    #Ceci est
    solutions=dict()
    triangMatrix=supTrigonization(arr,n)

    for i in range(0,n):
        solutions.__setitem__(f"x{i+1}", xiFormul(triangMatrix[i], i,triangMatrix,n))
    
    return solutions


