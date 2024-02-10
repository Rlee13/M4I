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

from MathNet.Numerics.LinearAlgebra.Double import DenseMatrix  # type: ignore

import System
from System import Double, Array


class M4I_Matrix(DenseMatrix):
    def __new__(self, rows, columns, arg0):
        __instance = super(M4I_Matrix, self).__new__(self, rows, columns, arg0)
        return __instance

    def __init__(self, rows, columns, arg0):
        super(M4I_Matrix, self).__init__()

        self.I = self.Inverse
        self.inverse = self.Inverse

        self.D = self.Determinant
        self.determinant = self.Determinant   

        self.rank = self.Rank
        self.range = self.Range

        self.clear = self.Clear

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
    """
    A class which represents a 3x3 matrix with elements of type 'double'.
        Usage:
            ret = Matrix3(arg)
        Parameters:
            arg (int/float): A integer/float
        Returns:
            a 3x3 Matrix with all elements initialized with 'arg' value
        Methods:
            from_list: initialize the Matrix from the content of a list of lists.
    """
    def __new__(self, arg0):
        __instance = super(MatrixD3x3, self).__new__(self, 3, 3, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
        return __instance

    def __init__(self, arg0):
        super(MatrixD3x3, self).__init__(3, 3, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
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

    @property
    def column_count(self):
        return self.__column_count

    @property
    def row_count(self):
        return self.__row_count

    def from_list(self, alist):
        """
        Initialize a 3x3 Matrix from the content of a list of lists. 
        The matrix has to be initialized first.
        Example:
            O.from_list([[1,1,1],
                         [1,2,3],
                         [4,3,2]])
        """
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
    """
    A class which represents a 4x4 matrix with elements of type 'double'.
        Usage:
            ret = Matrix4(arg)
        Parameters:
            arg (int/float): A integer/float
        Returns:
            a 4x4 Matrix with all elements initialized with 'arg' value
        Methods:
            from_list: initialize the Matrix from the content of a list of lists.
    """    
    def __new__(self, arg0):
        __instance = super(MatrixD4x4, self).__new__(self, 4, 4, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
        return __instance

    def __init__(self, arg0):
        super(MatrixD4x4, self).__init__(4, 4, Array[Double]((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
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

    @property
    def column_count(self):
        return self.__column_count

    @property
    def row_count(self):
        return self.__row_count

    def from_list(self, alist):
        """
        Initialize a 4x4 Matrix from the content of a list of lists. 
        The matrix has to be initialized first.
        Example:
            S.from_list([[1,1,1,2],
                         [1,2,3,5],
                         [4,3,2,6],
                         [9,2,4,5]
                        ])
        """
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
    

class MatrixDnxn(M4I_Matrix):
    """
    A class which represents a n x m matrix with elements of type 'double'.
        Usage:
            ret = MatrixN(rows, columns, arg)
        Parameters:
            rows (int): A integer representing the number of rows
            columns (int): A integer representing the number of columns
            arg (int/float): A integer/float
        Returns:
            a n x m Matrix with all elements initialized with 'arg' value
        Methods:
            from_list: initialize the Matrix from the content of a list of lists.
    """
    def __new__(self, rows, columns, arg0):
        __instance = super(MatrixDnxn, self).__new__(self, rows, columns, Array[Double]([arg0 for n in range(rows * columns)]))
        return __instance

    def __init__(self, rows, columns, arg0):
        super(MatrixDnxn, self).__init__(rows, columns, arg0)
        self.__column_count = columns
        self.__row_count = rows

    @property
    def column_count(self):
        return self.__column_count

    @property
    def row_count(self):
        return self.__row_count

    def from_list(self, alist):
        """
        Initialize a n x n Matrix from the content of a list of lists. 
        The matrix has to be initialized first.
        Example for a 5x5 matrix:
            S.from_list([[1,1,1,2,2],
                         [1,2,3,5,5],
                         [4,3,2,6,6],
                         [7,5,6,8,8],
                         [9,2,4,5,5]
                        ])
        """
        if not type(alist) == list: raise IndexError(f"List should be {self.row_count}x{self.column_count}")  # type: ignore
        if any([len(alist[x]) != self.column_count for x in range(self.row_count)]):
            raise IndexError(f"List should be {self.row_count}x{self.column_count}")  # type: ignore
        for i, row in enumerate(alist):
            for j, col in enumerate(row):
                self[i, j] = col
        return self
    