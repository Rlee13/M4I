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


from MathNet.Numerics import RootFinding, FindRoots  # type: ignore


class M4I_Roots(object):
    """
    A class to represent quadratic and cubic equations.
        Usage:
            R = Roots(0)
            # x^2 + x -2
            print(R.quadratic(1, 1, -2))
            # x^3 -3x^2 -6x +8   
            print(R.cubic(1, -3, -6, 8))
        Methods:
            quadratic - Find the roots of the quadratic equation 
                a*x^2 + b*x + c = 0.
            cubic - Find all three complex roots of the cubic equation 
                a*x^3 + b*x^2 + c*x + d = 0.
    """
    def __new__(self, arg0):
        __instance = super(M4I_Roots, self).__new__(self)
        return __instance

    def __init__(self, arg0):
        super(M4I_Roots, self).__init__()

    def cubic(self, a, b, c, d):
        """ Find all three complex roots of the cubic equation a*x^3 + b*x^2 + c*x + d = 0 """
        return RootFinding.Cubic.Roots(d, c, b, a)
    
    def quadratic(self, a, b, c):
        """ Find both complex roots of the quadratic equation a*x^2 + b*x + c = 0 """
        return FindRoots.Quadratic(c, b, a)