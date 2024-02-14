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

from MathNet.Numerics.LinearAlgebra.Double import DenseVector  # type: ignore

import System
from System import Double, Array

class M4I_Vector(DenseVector):
    def __new__(self, no_items, arg0):
        __instance = super(M4I_Vector, self).__new__(self, no_items)
        # __instance = super(M4I_Vector, self).__new__(self, Array[Double]([arg0 for n in range(no_items)]))
        return __instance

    def __init__(self, no_items, arg0):
        super(M4I_Vector, self).__init__()

        self.__count = no_items
        self.clear = self.Clear

    @property
    def count(self):
        return self.__count

class VectorD3(M4I_Vector):
    """
    A class which represents a 3x items vector with elements of type 'double'.
        Usage:
            ret = VectorD3(arg)
        Parameters:
            arg (int/float): A integer/float
        Returns:
            a 3x items Vector with all elements initialized with 'arg' value
        Methods:
            from_list: initialize the Vector from the content of a list.
    """     
    def __new__(self, arg0):
        __instance = super(VectorD3, self).__new__(self, 3, Array[Double]((arg0, arg0, arg0)))
        return __instance

    def __init__(self, arg0):
        # super(VectorD3, self).__init__(arg0)
        self.__count = 3
        self.__class__ = VectorDM

    #/** Print the vector X */
    def print_vector(self): 
        for n in self:
            print("\t" + n.ToString())
    
    def from_list(self, alist):
        """
        Initialize a 3x items Vector from the content of a list. 
        The Vector has to be initialized first.
        Example for a 3 items Vector:
            S.from_list([1,2,2])
        """        
        if not type(alist) == list or \
            len(alist) != 3:
                raise IndexError('List should have 3 elements')

        for i, vitem in enumerate(alist):
            self[i] = vitem
        return self 


class VectorD4(M4I_Vector):
    """
    A class which represents a 4x items vector with elements of type 'double'.
        Usage:
            ret = VectorD4(arg)
        Parameters:
            arg (int/float): A integer/float
        Returns:
            a 4x items Vector with all elements initialized with 'arg' value
        Methods:
            from_list: initialize the Vector from the content of a list.
    """     
    def __new__(self, arg0):
        if type(arg0) == list and len(arg0) == 4:
            __instance = super(VectorD4, self).__new__(self, 4, Array[Double]((arg0, arg0, arg0, arg0)))
        return __instance

    def __init__(self, arg0):
        # super(VectorD4, self).__init__(arg0)
        self.__count = 3
        self.__class__ = VectorDM

    #/** Print the vector X */
    def print_vector(self): 
        for n in self:
            print("\t" + n.ToString())
    
    def from_list(self, alist):
        """
        Initialize a 4x items Vector from the content of a list. 
        The Vector has to be initialized first.
        Example for a 4 items Vector:
            S.from_list([1,2,2,3])
        """        
        if not type(alist) == list or \
            len(alist) != 4:
                raise IndexError('List should have 34 elements')

        for i, vitem in enumerate(alist):
            self[i] = vitem
        return self 
    

class VectorDM(M4I_Vector):
    """
    A class which represents a m items vector with elements of type 'double'.
        Usage:
            ret = VectorDM(no_items, arg)
        Parameters:
            no_items (int): A integer representing the number of items
            arg (int/float): A integer/float
        Returns:
            a m items Vector with all elements initialized with 'arg' value
        Methods:
            from_list: initialize the Vector from the content of a list.
    """    
    def __new__(self, no_items, arg0):
        __instance = super(VectorDM, self).__new__(self, no_items, Array[Double]([arg0 for n in range(no_items)]))
        # __instance = super(VectorDM, self).__new__(self, no_items)
        return __instance

    def __init__(self, no_items, arg0):
        super(VectorDM, self).__init__(no_items, Array[Double]([arg0 for n in range(no_items)]))
        self.__count = no_items

    #/** Print the vector X */
    def print_vector(self): 
        for n in self:
            print("\t" + n.ToString())
    
    def from_list(self, alist):
        """
        Initialize a m items Vector from the content of a list. 
        The Vector has to be initialized first.
        Example for a 5 items Vector:
            S.from_list([1,1,1,2,2])
        """
        if not type(alist) == list or len(alist) != self.count:
            raise IndexError(f"List should have {self.count} elements") # type: ignore

        for i, vitem in enumerate(alist):
            self[i] = vitem
        return self    