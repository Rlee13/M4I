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
from MathNet.Numerics import Control,LinearAlgebra
from MathNet.Numerics.LinearAlgebra.Double import DenseVector

import System
from System import Double, Array

class M4I_Vector(DenseVector):
    def __new__(self, arg0):
        #print "M4I_Vector Creating Instance ", arg0
        __instance = super(M4I_Vector, self).__new__(self, arg0)
        return __instance

    def __init__(self, arg0):
        # super(M4I_Vector, self).__init__(arg0)
        super(M4I_Vector, self).__init__()


class Vector3(M4I_Vector):
    def __new__(self, arg0):
        #print "__new__Vector3 Creating Instance", arg0
        if type(arg0) == list and len(arg0) == 3:
            _a = Array[Double]((arg0[0], arg0[1], arg0[2]))
            __instance = super(Vector3, self).__new__(self, _a)
        else:
            __instance = super(Vector3, self).__new__(self, 3)
        return __instance

    def __init__(self, arg0):
        super(Vector3, self).__init__(arg0)
        #print "__init__Vector3", type(arg0)
        self.__column_count = 3

    @property
    def column_count(self):
        return self.__column_count


    # def create(self):
    #     _mat = Vector3.Build.Dense(3)
    #     return _mat

    # def create_random(self):
    #     _mat = Vector3.Build.Random(3)
    #     return _mat

    #/** Print the vector X */
    #def printVector(prompt, X): 
    def print_vector(self): 
        #print (prompt)
        for n in self:
            print("\t" + n.ToString())
    
    def from_list(self, alist):
        if not type(alist) == list or \
            len(alist) != 3:
                raise IndexError('List should have 3 elements')
                #print errorStrings[0]
                #sys.exit()
        for i, row in enumerate(alist):
            for j, col in enumerate(row):
                self[i, j] = col
        return self