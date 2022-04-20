def derivee(fonc, x0, epsilon=10e-10):
    der=(fonc(epsilon+x0)-fonc(x0))/epsilon
    if der==0: 
        # print(f"derivee=0 {der}")
        return 1
    else: return der