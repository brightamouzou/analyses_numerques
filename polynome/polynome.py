class Polynome:
    def __init__(self,n,args):
            self.degre=n

            #ceoffs represente les coefficients du polynome : dans l'ordre a0, a1, a2...
            self.coeffs=Polynome.coefficientsHash(args)
    @classmethod
    def coefficientsHash(self, args:list):
        tmp={}
        for k,v in enumerate(args):
            tmp[f"{k}"]=v
        return tmp

    @classmethod
    def productOfTwoPolynoms(self, pol1, pol2):
        maxDeegrePlynome=pol1
        minDeegrePlynome=pol2
        if pol1.degre<pol2.degre:
            maxDeegrePlynome=pol2
            minDeegrePlynome=pol1

        polynomsArr=[]
        for i in range(minDeegrePlynome.degre+1):
            polynomsArr.append(Polynome(maxDeegrePlynome.degre+i ,[0]*i + [minDeegrePlynome.coeffs[f"{i}"]*float(k) for k in list(maxDeegrePlynome.coeffs.values())]) )
        return Polynome.sumOfPolynoms(polynomsArr)
    
    @classmethod
    def productOfPolynoms(self, polynomsArr):
        p=polynomsArr[0]
        for i in range(1,len(polynomsArr)):
            p=Polynome.productOfTwoPolynoms(p, polynomsArr[i])
        
        return p
        
    @classmethod
    def sumOfPolynoms(self, polynomsArr):
        p=polynomsArr[0]
        for i in range(1,len(polynomsArr)):
            p=Polynome.sumOfTwoPolynoms(p, polynomsArr[i])
        return p

    @classmethod 
    def sumOfTwoPolynoms(self, pol1,pol2):
        #Je trie d'abord le tableaumaxDeegrePlynome=pol1
        maxDeegrePlynome=pol1
        minDeegrePlynome=pol2
        if pol1.degre<pol2.degre:
            maxDeegrePlynome=pol2
            minDeegrePlynome=pol1   
        # polynomsArr=sorted(polynomsArr, key=lambda x: x.degre)
        
        # maxDeegrePlynome=polynomsArr[-1]
        # minDeegrePlynome=polynomsArr[0]
        # print(polynomsArr)
        minDeegre=minDeegrePlynome.degre+1
        maxDeegre=maxDeegrePlynome.degre+1
        endArr=[]

        

        #NB: le degre du plonynome represente le nombre de coefficients moins 1 (Il y a beaucoup de decuctions à faire dans cet algo)

        #Je somme deux à deux les les coefficients des deux polynomes pour obtenir le polynome de sortie
        for i in range(minDeegre):
            endArr.append(sum([ float(k.coeffs[f"{i}"]) for k in [pol1, pol2] ]))




        """
            La boucle precendente somme les elements deux a deux mais s'arrete aux ceoficients du  polynome du plus petit degre
            exemple: (2+3x) +(1+5x+4x^2) ->les nouveaux coefficients à la fin de cette seront juste [3, 8]
            Il va falloir ajouter au tableau les coefficients restants du polynomes de degre le plus grand qui n'ont pas trouvé de correspondant
            Cele se fera si et seulement si les degres des deux polynomes sont differernts
        """
        if (minDeegre!=maxDeegre):endArr.extend(list( maxDeegrePlynome.coeffs.values() )[minDeegre:])

        return Polynome(maxDeegrePlynome.degre, endArr)

        # while minDeegre < maxDeegre:
        #     endArr.append(sum(k.coeffs[f"{minDeegre}"] for k in polynomsArr[minDeegre-1:]))
        #     minDeegre+=1       
        # return endArr
    

    def productWithConstant(self,constant):
        coeffs=self.coeffs
        self.coeffs=dict(map(lambda x: (x,coeffs[x]*constant), coeffs))

        
    def __repr__(self) -> str:
        # print({"degre":self.degre, "coeffs":self.coeffs})
        return {"degre":self.degre, "coeffs":self.coeffs}.__str__()


    @classmethod
    def printPolynom(self, coeffs):
        endStr=[]
        for k,v in enumerate(coeffs):
            if abs(v)>10e-4:
                endStr.append(f"( {v}x^{k}) ")
        print("P(X)= "+" + ".join(endStr))

# k=Polynome(0, [1])
# k2=Polynome(3, [2,-3,1,-5])
# k3=Polynome(2, [1,-1, .5])

# k2.productWithConstant(2.5)

# print(k2)

# print(Polynome.productOfTwoPolynoms(k2, k).__dict__)

# print(Polynome.sumOfTwoPolynoms(k, k2))
# print(Polynome.productOfPolynoms([k,k2,k3]))
# print(p.__dict__)

