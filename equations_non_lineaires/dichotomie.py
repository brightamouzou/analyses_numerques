# f=lambda x:  x**2 - 1
def balayage(f,a,b, step):
    solutionsIntervals=[]
    try:
        if f(a)==0: solutionsIntervals.append([a])
    except ZeroDivisionError:
        a+=10e-10
        balayage(f,a,b,step)
    try:
        if f(b)==0: solutionsIntervals.append([b])
    except ZeroDivisionError:
        b-=10e-10
        balayage(f,a,b,step) 
    tmp=a    
    try:
        while tmp<b:
            nextStep=tmp+step
            try:
                if f(nextStep)*f(tmp)<0:
                    solutionsIntervals.append([tmp,nextStep])
            except:
                pass
            tmp+=step
    except: 
        pass

    return solutionsIntervals 
    

def dichotomie(f, a, b, epsilon=10e-10,stepBalayage=0.001, nbItMax=20):

    if b<a:
        ans=input(f"Intervalle invalide (b<a) . Voulez vous dire [{b}, {a}] ? (o/n)")
        if ans.lower()=="o":return dichotomie(f, b, a)
        else: return "Aucune solution trouvée"
    elif b==a:
        if f(a)==0:
            return a
        else:
            return f"Votre intervalle se resule en point : x={a}. Aucune solution trouvée trouvée en ce point. Tentez de saisir un intervalle valide "
    
        


    try:
        
        if f(a)==0: return a
    except ZeroDivisionError:
        #On continue
        pass        
    try:
        if f(b)==0: return b
    except ZeroDivisionError:
        #On passe au balayage
       pass



    solutionsIntervals=balayage(f,a,b,stepBalayage)
    # solutionsIntervals=[[a,b]]

    solutions={}
    for k,v in enumerate(solutionsIntervals):
        if len(v)==1:
            solutions[f'x{k}']= v[0]
        else:
            tmpA =v[0]; tmpB=v[1]
            try:
                iterations=0
                milieu=(tmpA+tmpB)/2
                # while abs(f(milieu))>epsilon and iterations<nbItMax : 
                #     milieu=(tmpA+tmpB)/2
                #     if f(milieu) ==0: return milieu
                #     if( f(tmpA)*f(milieu)<=0):
                #         tmpB=milieu
                #     else:
                #         tmpA=milieu
                    
                #     iterations+=1
                mil=(tmpA+tmpB)/2
                while((tmpB-tmpA)>epsilon):
                    if f(mil)==0:
                        return mil
                    
                    elif(f(mil)*f(tmpA)<0):
                        tmpB=mil
                        mil=(tmpA+tmpB)/2            
                    else:
                        tmpA=mil
                        mil=(tmpA+tmpB)/2
                    #verifier si la fonction est continue en ce point
                    try:
                        t1=float(str(mil)[:5])+stepBalayage
                        t2=float(str(mil)[:5])
                        t3=float(str(mil)[:5])-0.01

                        a,b,c=f(t1), f(t2), f(t3)
                        
                    except ZeroDivisionError:
                        pass
                    else:
                        solutions[f'x{k}']= mil
                
            except:
                continue
    return solutions if len(solutions)>0 else "Aucune solution"
            
            

        
    
if __name__=="__main__":
    print(dichotomie(f,-2,2,10e-3))