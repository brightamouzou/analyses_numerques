def factorize(line:list, lineNum):
    return list(map(lambda x: x/line[lineNum], line))
    

def factorisation(mat:list):
    for k,v in enumerate(mat):
        mat[k]=factorize(v, k)
    return mat

def gaussJordan(mat:list):#mat=inf mat
    factorizedMat=[k[-1]for k in factorisation(mat)]
    #On recupère les bi(i allant de 1 à n) de la matrice factorisée. Ces bi representent la solution

    solutions=dict()
    for k,v in enumerate(factorizedMat):
        solutions.__setitem__(f"x{k+1}", v)

    return solutions
    
    # return dict(map(lambda x: (f'x{factorizedMat.index(x)+1}', x), factorizedMat))


