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


from MathNet import Numerics  # type: ignore
from MathNet.Numerics import Control,LinearAlgebra  # type: ignore
from MathNet.Numerics.LinearAlgebra.Double import DenseMatrix  # type: ignore

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

        self.I = self.Inverse
        self.inverse = self.Inverse

        self.D = self.Determinant
        self.determinant = self.Determinant   

        self.rank = self.Rank
        self.range = self.Range

    def __getitem__(self, key):
        if isinstance(key, int):
            return super().__getitem__(key)
        elif isinstance(key, tuple):
            (row, cols) = key
            if isinstance(row, slice) and isinstance(cols, slice):
                if row.step or cols.step:
                    raise NotImplementedError("'step' in slice not implemented.")
                return self.SubMatrix(row.start, row.stop - row.start + 1, 
                                      cols.start, cols.stop - cols.start + 1)
            return super().__getitem__(row, cols)
        else:
            raise TypeError(f"{type(self).__name__} indices must be integers or slices, not {type(key).__name__}") # type: ignore
        
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            (row, cols) = key
            if isinstance(row, slice) and isinstance(cols, slice):
                if row.step or cols.step:
                    raise NotImplementedError("'step' in slice not implemented.")
                if (((row.stop - row.start + 1) != value.RowCount) or 
                    ((cols.stop - cols.start +1) != value.ColumnCount)):
                    raise IndexError("source and destination must have the same dimensions.")
                return self.SetSubMatrix(row.start, cols.start, value)
            super().__setitem__(row, cols, value)
        else:
            raise TypeError(
                f"{type(self).__name__} indices must be integers or slices, not {type(key).__name__} and value must be a Matrix") # type: ignore
        
    
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
            super(MatrixD3x3, self).__init__(3, 3, arg0)
        else:
            raise IndexError("The list should be 3x3, or the argument should be int or float.")
        self.__column_count = 3
        self.__row_count = 3

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

    def clear(self):
        self.ClearRow(0); self.ClearRow(1); self.ClearRow(2)
        return self

    def from_list(self, alist):
        if not type(alist) == list or \
            len(alist) != 3 or \
            len(alist[0]) != 3 or \
            len(alist[1]) != 3 or \
            len(alist[2]) != 3 :
                raise IndexError('List should be 3x3')

        for i, row in enumerate(alist):
            for j, col in enumerate(row):
                self[i, j] = col
        return self


class MatrixD4x4(M4I_Matrix):
    def __new__(self, arg0):
        # print ("MatrixD4x4 Creating Instance", arg0)
        __instance = super(MatrixD4x4, self).__new__(self, 4, 4, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
        # __instance = super(MatrixD4x4, self).__new__(self, 4, 4, 0.0)
        return __instance

    def __init__(self, arg0):
        super(MatrixD4x4, self).__init__(4, 4, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
        # super(MatrixD4x4, self).__init__(4, 4, 0.0)
        # print ("__init__MatrixD4x4", arg0)
        if type(arg0) == list and len(arg0) == 4 and len(arg0[0]) == 4 and len(arg0[1]) == 4 and len(arg0[2]) == 4 and len(arg0[3]) == 4 :
            self[0,0] = arg0[0][0]; self[0,1] = arg0[0][1]; self[0,2] = arg0[0][2]; self[0,3] = arg0[0][3]
            self[1,0] = arg0[1][0]; self[1,1] = arg0[1][1]; self[1,2] = arg0[1][2]; self[1,3] = arg0[1][3]
            self[2,0] = arg0[2][0]; self[2,1] = arg0[2][1]; self[2,2] = arg0[2][2]; self[2,3] = arg0[2][3]
            self[3,0] = arg0[3][0]; self[3,1] = arg0[3][1]; self[3,2] = arg0[3][2]; self[3,3] = arg0[3][3]
        elif type(arg0) == int or type(arg0) == float:
            super(MatrixD4x4, self).__init__(4, 4, arg0)
        else:
            raise IndexError("The list should be 4x4, or the argument should be int or float.")
        self.__column_count = 4
        self.__row_count = 4

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

    def clear(self):
        self.ClearRow(0); self.ClearRow(1); self.ClearRow(2); self.ClearRow(3)
        return self

    def from_list(self, alist):
        if not type(alist) == list or \
            len(alist) != 4 or \
            len(alist[0]) != 4 or \
            len(alist[1]) != 4 or \
            len(alist[2]) != 4 or \
            len(alist[3]) != 4 :
                raise IndexError('List should be 4x4')
        for i, row in enumerate(alist):
            for j, col in enumerate(row):
                self[i, j] = col
        return self