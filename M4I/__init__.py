__version_info__ = (0, 0, 1)
__version__ = '.'.join([str(num) for num in __version_info__])
__version__ = __version__ + '-alpha6'
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
Vector3 = m4i_vector.Vector3
Roots = m4i_root_finding.M4I_Roots
Precision = m4i_precision



