#!/usr/bin/python3.8
from itertools import permutations
from gauss import gauss
from gaussJordan import gaussJordan
from utils import *
import numpy as np
import sys
from copy import deepcopy
n=0


def initializeLU(newN):
    global n
    #Vauleur de la variable globale n changée avec newN
    n=newN
    l=[]
    u=[]
    for i in range(n):
        u.append([0]*n)
        l.append([0]*n)
        u[i][i]=1
    return l,u
        


# for i in range(n):
#     a.append([int(q) for q in input().split()])


#Determination  de li1

def findLU(l:list, u:list,a:list,b:list):
    n=len(l)

    #Si a[i][i]==0 ->permutation
    if a[0][0]==0:
        permuationMatrix(a, 0,b)

    for i in range(n):
        l[i][0]=a[i][0]

    #Determinbation de u1i
    for i in range(1,n):
        u[0][i]=a[0][i]/l[0][0]
        


    for i in range(1,n-1):

        # if a[i][i]==0:
        #     permuationMatrix(a,i)
        # l[i][i]=a[i][i]-sum([l[i][k]*u[k][i] for k in range(i-1)])
        for j in range(i, n):
            l[j][i]=a[j][i]-sum([l[j][k]*u[k][i] for k in range(0,j)])

            
        print(l[i][i])
        for j in range(i+1, n):
            # if l[i][i]==0:

            if l[i][i]==0:
                print("l[i,i]==0")
                permuationMatrix(a,i,b)
                permuationMatrix(l,i)
        
            if l[i][i]==0:
                # print("i: ",i)
                # print("abefore", a)
                # print("hoyee")
                # permuationMatrix(a,i,b)
                # print("aafter", a)

                # print("lbefore", l)
                permuationMatrix(l,i)
                print("lzfter",l,end="\n\n")

                

            u[i][j]=( a[i][j] - sum([l[i][k]*u[k][j] for k in range(j)]))/l[i][i]

    l[n-1][n-1]=a[n-1][n-1] - sum([l[n-1][k]*u[k][n-1] for k in range(n-1)])
    print("lfibzl",l)
    print("ufinzl",u)

#Ajouter un element en fin de tableau
def appendList(x:list, elmt):
    x.append(elmt)
    return x

def extendMatrixItems(l:list, matB:list):
    tmpList=deepcopy(l)
    #Ajouter bi à chacune des lignes de la amtrice l
    newList= list( map(lambda  x:appendList(x, matB[l.index(x)]), tmpList))
    return newList

"""
    Après la decomposition de la matrice A en L et U, j'utilise cette fonction pour resoudre Ly=b et ux=y

    L=matrice inferieure
    U=matrice superieure
"""
def LYEqualsToB(infMatL:list, matB):
    newL=extendMatrixItems(infMatL, matB)
    newL=supTrigonization(deepcopy(newL),n)

    #L est un ematrice triangulaire inferieure , donc je resouds l'equation avec la methode de Gauss jordan
    return gaussJordan(newL)

def UXEqualsToY(supMatU:list, matB):
    newL=extendMatrixItems(supMatU, matB)
    #U est un ematrice triangulaire supereure , donc je resouds l'equation avec la methode de Gauss
    diag=infTrigonization(newL,len(supMatU))
    return gauss(diag, len(supMatU))


def lu(l,u,matB):
    y=LYEqualsToB(l, matB)
    #y est un dictionnaire de la fomre {'x1':val1, 'x2':val2, ...} dans mon cas ici, je recupère les valeurs val1, val2, ...
    x=UXEqualsToY(u,list(y.values()))
    return x


    



