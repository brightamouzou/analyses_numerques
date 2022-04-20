#!/usr/bin/python3.8
import os
import sys
import numpy as np
from copy import deepcopy
from thomas import thomas
from gauss import * 
from gaussJordan import * 
from jacobi import * 
from gaussSeidel import * 
from utils import * 
from lu import *
from choleski import *
sys.stdin=open("mat.txt", "r")

r,c=os.popen("stty size", "r").read().split()

"""
    Por les methodes de dauss et gauss-jordan, on utilise une matrice carrée A mais on ajoute à la fin de chaque ligne le b correspondant
    donc on a:

    a=
    [
        [a11, a22, ..., a1n, b11]
                .   .
                .   .
                .   .
                .   .
        [an1, an2, ..., ann, bn1]
    ]

    Par contre pour la methode LU, on utilise juste la matrice carrée A
    donc on a:

    a=
    [
        [a11, a22, ..., a1n]
                .   .
                .   .
                .   .
                .   .
        [an1, an2, ..., ann]
    ]


"""
             
n=int(input())
a=[]
b=[]
for i in range(n):
    # print(f"Veuillez saisir les éléments de la colonne {j+1} separés par des espaces")
    a.append([int(k) for k in input(f"Colonne {i+1}:").split()])

b=[int(i) for i in input().split()]

#Je fais la copie de la matrice a et une colonne(bi) à chacune de ces lignes . Cete colonne correspond à bi
copyOfA= list(map(lambda x :[*x, b[a.index(x)]], deepcopy(a)))
copyOfB=  deepcopy(b)

#for gauss and gauss-jordan
mat1=supTrigonization(copyOfA,n)
mat2=infTrigonization(mat1, n)

#for lu
l, u=initializeLU(n)
findLU(l,u, deepcopy(a),deepcopy(b))

# Pour jacobi et gauss-seidel
#J'evite d'utiliser la matrice A ou B elles meme pour eviter que ca agisse sur mes autres methodes 
initializeAandBJacobi(deepcopy(a),deepcopy(b), n)
initializeAandBGaussSeidel(deepcopy(a) ,deepcopy(b),n)



print("*************Methodes directes*************".center(int(c), " "))
print("\n\nGAUSS: ",gauss(copyOfA, n))
print("\n\nGAUSS-JORDAN: ",gaussJordan(mat2))
print("\n\nLU (CROUT): ", lu(l, u, deepcopy(b)))
print("\n\nCHOLESKY: ",cholesky( deepcopy(a) , deepcopy(b) ))
print("\n\nTHOMAS: ",thomas( deepcopy(a) , deepcopy(b)))

print("\n\n","*************Methodes iteratives*************".center(int(c), " "))

X0=[0,0,0]
print("\n\nJACOBI: ", jacobi(X0, 10e-10))
print("\n\nGAUSS-SEIDEL: ", gaussSeidel(X0, 10e-10))



