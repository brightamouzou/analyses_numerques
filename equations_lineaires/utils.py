from copy import deepcopy
from numpy import mat



def supTrigonization(arr:list,n:int):
    b=deepcopy(arr)
    c=[[0]*(n+1)]*n

    # if not arr[0][0]:
        # raise ValueError("Matrice non inervsible")
        # permuation
    for i in range(n-1):
        pivot=b[i][i] 

        if pivot==0:
            permuationMatrix(b,i)
            pivot=b[i][i]


        for k in range(i+1, n):
            tmpArr=[]
            for q in range(n+1):#n+1 pârce que le vecteur b aussi doit en beneficier
                """
                    Pour chaque ligne lk , on change la valeur de chaque colonne selon la formule générale : lk <- lk - (aki/aii)*li
                    lk=ligne numero k
                    li represente la ligne du pivot
                """ 

                tmpArr.append( b[k][q] - (b[k][i] / pivot) * b[i][q] )
            b[k]=tmpArr.copy()
    return b


def infTrigonization(mat:list,n:int)->list:
    b=mat.copy()
    
    for i in range(n-1, 0, -1):
        pivot=b[i][i]
        # print("pivot",pivot)

        if pivot==0:
            permuationMatrix(mat, i)
        # if pivot==0:
        #     raise ValueError("Matrice non versible. Pas de solution")
                    
        for k in range(i-1,-1, -1):
            tmpArr=[]
            for q in range(n+1):
                tmpArr.append( b[k][q] - (b[k][i]/pivot)*b[i][q])
            b[k]=tmpArr.copy()
    return b


def permuationVector(b:list, i, j):
    
    if(b==None):
        return 
    b[i], b[j]=b[j], b[i]


def permuationMatrix(mat,numLine, b=None):

    i=numLine;l=len(mat)
        # print("yoo")
    j=i+1
    while mat[j][i]==0:
        # print(mat, end="\n\n")
        j+=1
    
    if j!=len(mat):
        mat[j],mat[i]=mat[i], mat[j]
        permuationVector(b, i, j)

    else:
        raise ValueError("Impossible, La matrice n'est pas inversible")
        # print("yi")

        # j=0
        # while mat[j][i]==0 and j<l:
        #     print("yi")
        #     j+=1

        # if j==l:
        #     raise ValueError("Impossible, La matrice n'est pas inversible")
        # else:
        # # else j<l:
        #     mat[i],mat[j]=mat[j], mat[i]
        #     permuationVector(b, i, j)

    
#Ajouter un element en fin de tableau
def appendList(x:list, elmt):
    x.append(elmt)
    return x


        
def extendMatrixItems(l:list, matB:list):
    tmpList=deepcopy(l)
    #Ajouter bi à chacune des lignes de la amtrice l
    newList= list( map(lambda  x:appendList(x, matB[l.index(x)]), tmpList))
    return newList