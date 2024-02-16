__version_info__ = (0, 0, 1)
__version__ = '.'.join([str(num) for num in __version_info__])
__version__ = __version__ + '-alpha8'
__author__ = "RLee"
__repository__ = "https://github.com/Rlee13/M4I"

__all__ = [
    'm4i_matrix',
    'm4i_vector',
    'm4i_root_finding',
    'm4i_precision',
    'm4i_settings'
    ]


dependencies = ''' 

    ERROR:: This module requires MathNet.Numerics.dll,
    MathNet.Numerics.MKL.dll

'''

from . import m4i_settings as SG

import sys, os
try:
    sys.path.append(os.getcwd() + os.sep + SG.ASSEMBLIES_PATH)
    import clr
    clr.AddReference('MathNet.Numerics')
except IOError:
    print(dependencies)
    sys.exit()

from . import m4i_matrix, m4i_vector, m4i_root_finding, m4i_precision

MatrixD3 = m4i_matrix.MatrixD3x3
MatrixD4 = m4i_matrix.MatrixD4x4
MatrixDMN = m4i_matrix.MatrixDmxn
VectorD3 = m4i_vector.VectorD3
VectorDM = m4i_vector.VectorDM
Roots = m4i_root_finding.M4I_Roots
Precision = m4i_precision

def delete(arr, obj, axis = None):
    """
    Returns an MatrixDmxn with sub-rows/columns specified by obj deleted. 
    For a VectorDM or one dimensional MatrixDmxn, the axis parameter is ignored.
    Parameters:
        arr : Input matrix or vector.
        obj: A slice, a int or list of integers - indicates indices to remove along the 
            specified axis.
        axis: An integer, optional - for axis = 0 or 1, the removal of items is done 
            by row or by column respectively. 
        If axis = None, removal of items is applied to the flattened array (Not Implemented).
    Returns:
        out_matrix :  MatrixDmxn or VectorDM - a copy of arr with the elements specified 
            by obj removed. 
    """
    if isinstance(arr, MatrixDMN):
        _ret = None
        if axis == 0:
            if isinstance(obj, int):
                _ret = arr.RemoveRow(obj)
                _ret0 = MatrixDMN(_ret.RowCount, _ret.ColumnCount,0)
                _ret.CopyTo(_ret0)
                return _ret0
            elif isinstance(obj, list):
                i = 0
                if len(obj) == 0: return arr
                _ret = MatrixDMN(arr.RowCount - len(obj), arr.ColumnCount,0)
                for x in range(arr.RowCount):
                    if x not in obj:
                        _ret.SetRow(i, arr.Row(x))
                        i += 1
                return _ret
        elif axis == 1:
            if isinstance(obj, int):
                _ret = arr.RemoveColumn(obj)
                _ret0 = MatrixDMN(_ret.RowCount, _ret.ColumnCount,0)
                _ret.CopyTo(_ret0)
                return _ret0
            elif isinstance(obj, list):
                i = 0
                if len(obj) == 0: return arr
                _ret = MatrixDMN(arr.RowCount, arr.ColumnCount - len(obj),0)
                for x in range(arr.ColumnCount):
                    if x not in obj:
                        _ret.SetColumn(i, arr.Column(x))
                        i += 1
                return _ret
        else:
            raise NotImplementedError(f"Flattened array is not implemented.") # type : ignore
        
    elif isinstance(arr, VectorDM):
        _ret = []
        if isinstance(obj, int):
            for i, x in enumerate(arr):
                if i != obj: _ret.append(x)
            _v = VectorDM(len(arr) - 1, 0)
            _v.from_list(_ret)
            return _v
        elif isinstance(obj, list):
            for i, x in enumerate(arr):
                if i not in obj: _ret.append(x)
            # print(len(arr), len(_ret))
            _v = VectorDM(len(_ret), 0)
            _v.from_list(_ret)
            return _v
        elif isinstance(obj, slice):
            [_ret.append(x) for x in arr]
            del _ret[obj]
            _v = VectorDM(len(_ret), 0)
            _v.from_list(_ret)
            return _v
    else:
        raise NotImplementedError(f"delete is not implemented for {type(arr)}.") # type : ignore