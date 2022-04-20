import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname( os.path.dirname(__file__)))
sys.path.append(os.path.dirname( os.path.dirname(os.path.dirname(__file__))))

from numerical_analysis.interpolation.moindre_carre import moindreCarres
from numerical_analysis.interpolation.newton import interpolationNewton
from numerical_analysis.interpolation.lagrange import *
n=7


# ----------------------------------
# x | 3|...|  |  |  |  |  |  |  |  |  |
# -----------------------------------
# y| -0.905 |...  |  |  |  |  |  |  |  |  |  |
# -----------------------------------

# has set of keys value x,y
vals={-3:-0.90514,  -2:-0.7615,  -1:-0.46211,  0:0,  1:0.46211, 2:0.76159, 3:0.90514}

# vals={(-3,-26/7),  (-2,-7/3),  (-1,0),  (0,1),  (1,2/3), (2,9/7), (3,28/13)}

interpolationLagrange(n, vals)
interpolationNewton(n, vals)
moindreCarres(n-1, vals)