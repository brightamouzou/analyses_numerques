from cmath import sqrt
import math
from fixedPoints import fixedPoints
from newton import newton
from secante import secante
from dichotomie import dichotomie


# f=lambda x: x**3 +5*x**2 + 8*x -3
f=lambda x: x**2 -5*x + 6
g=lambda x:(x**2+6)/5
# g=lambda x:sqrt(5*x - 6)

a,b=0,1
x0,x1=0,1

print("\n\nNEWTON : ",newton(f, x0)) 
print("\n\nSECANTE : ",secante(f, x0,x1))
print("\n\nDICHOTOMIE : ",dichotomie(f, a,b))
print("\n\nPOINTS FIXES : ",fixedPoints(g, x0))

