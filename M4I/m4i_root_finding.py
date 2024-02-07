import sys, clr

dependencies = ''' 

    ERROR:: This module requires MathNet.Numerics.dll,
    MathNet.Numerics.MKL.dll

'''
try:
    clr.AddReference('MathNet.Numerics')
except IOError:
    print (dependencies)
    sys.exit()


from MathNet import Numerics
from MathNet.Numerics import RootFinding, FindRoots


class M4I_Roots(object):
    def __new__(self, arg0):
        #print "M4I_Roots Creating Instance ", arg0
        # __instance = super(M4I_Roots, self).__new__(self, arg0)
        __instance = super(M4I_Roots, self).__new__(self)
        return __instance

    def __init__(self, arg0):
        # super(M4I_Roots, self).__init__(arg0)
        super(M4I_Roots, self).__init__()

    #
    # Find all three complex roots of the cubic equation a*x^3 + b*x^2 + c*x + d = 0.
    # 
    def cubic(self, a, b, c, d):
        """ Find all three complex roots of the cubic equation a*x^3 + b*x^2 + c*x + d = 0 """
        return RootFinding.Cubic.Roots(d, c, b, a)
    
    #
    # Find the roots of the quadratic equation a*x^2 + b*x + c = 0.
    # 
    def quadratic(self, a, b, c):
        """ Find both complex roots of the quadratic equation a*x^2 + b*x + c = 0 """
        return FindRoots.Quadratic(c, b, a)