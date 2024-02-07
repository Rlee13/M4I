import sys, clr

errorStrings = [
    "Error :: Index error, list should be 3x3"
    ]

dependencies = ''' 

    ERROR:: This module requires MathNet.Numerics.dll,
    MathNet.Numerics.MKL.dll.

'''
try:
    clr.AddReference('MathNet.Numerics')
except IOError:
    print (dependencies)
    sys.exit()


from MathNet import Numerics
from MathNet.Numerics import Control,LinearAlgebra
from MathNet.Numerics.LinearAlgebra.Double import DenseMatrix

import System
from System import Double, Array


class M4I_Matrix(DenseMatrix):
    def __new__(self, rows, columns, arg0):
        # print ("M4I_Matrix Creating Instance ", arg0)
        __instance = super(M4I_Matrix, self).__new__(self, rows, columns, arg0)
        return __instance

    def __init__(self, rows, columns, arg0):
        # print("M4I_Matrix Init Instance ", rows, columns, arg0)
        # super(M4I_Matrix, self).__init__(rows, columns, arg0)
        super(M4I_Matrix, self).__init__()

    
class MatrixD3x3(M4I_Matrix):
    def __new__(self, arg0):
        # print ("MatrixD3x3 Creating Instance", arg0)
        __instance = super(MatrixD3x3, self).__new__(self, 3, 3, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
        return __instance

    def __init__(self, arg0):
        super(MatrixD3x3, self).__init__(3, 3, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
        # print ("__init__MatrixD3x3", arg0)
        if type(arg0) == list and len(arg0) == 3 and len(arg0[0]) == 3 and len(arg0[1]) == 3 and len(arg0[2]) == 3 :
            self[0,0] = arg0[0][0]; self[0,1] = arg0[0][1]; self[0,2] = arg0[0][2]
            self[1,0] = arg0[1][0]; self[1,1] = arg0[1][1]; self[1,2] = arg0[1][2]
            self[2,0] = arg0[2][0]; self[2,1] = arg0[2][1]; self[2,2] = arg0[2][2]
        elif type(arg0) == int or type(arg0) == float:
            self[0,0] = arg0; self[0,1] = arg0; self[0,2] = arg0
            self[1,0] = arg0; self[1,1] = arg0; self[1,2] = arg0
            self[2,0] = arg0; self[2,1] = arg0; self[2,2] = arg0
        else:
            raise IndexError("The list should be 3x3, or the argument should be int or float.")
        self.__column_count = 3
        self.__row_count = 3
        self.I = self.inverse()

    #def __repr__(self):
    #    return "Test()"

    # def __str__(self):
    #    return str(self[i,j] for i in self for j in self[0,:])

    #def __add__(self, another_matrix):
    #    return self + another_matrix

    @property
    def column_count(self):
        return self.__column_count

    @property
    def row_count(self):
        return self.__row_count

    # def create(self):
    #     _mat = MatrixD3x3(0)
    #     return _mat

    # def create_random(self):
    #     _mat = MatrixD3x3.Build.Random(3, 3)
    #     return _mat
    
    #def print_matrix3(self):
    #    #for i in range(3):
    #    #    for j in range(3):
    #    #        print("\t" + self[i,j].ToString())
    #    for i in range(3):
    #    #for j in range(3):
    #        self.Row(i).print_vector()

    def inverse(self):
        _mat = self.Inverse()
        return _mat

    def determinant(self):
        _mat = self.Determinant()
        return _mat

    def clear(self):
        _mat.ClearRow(0); _mat.ClearRow(1); _mat.ClearRow(2)
        return _mat

    def from_list(self, alist):
        if not type(alist) == list or \
            len(alist) != 3 or \
            len(alist[0]) != 3 or \
            len(alist[1]) != 3 or \
            len(alist[2]) != 3 :
                raise IndexError('List should be 3x3')
                #print errorStrings[0]
                #sys.exit()
        for i, row in enumerate(alist):
            for j, col in enumerate(row):
                self[i, j] = col
        return self