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

from MathNet.Numerics import Precision  # type: ignore

# The number of significant decimal places of double-precision floating numbers (64 bit).
DOUBLE_DECIMAL_PLACES = Precision.DoubleDecimalPlaces

# Standard epsilon, the maximum relative precision of IEEE 754 double-precision floating numbers (64 bit).
# According to the definition of Prof. Demmel and used in LAPACK and Scilab.
DOUBLE_PRECISION = Precision.DoublePrecision

# Actual double precision machine epsilon, the smallest number that can be subtracted from 1, yielding a results different than 1.
# This is also known as unit roundoff error. According to the definition of Prof. Demmel.
# On a standard machine this is equivalent to `DoublePrecision`.
MACHINE_EPS = Precision.MachineEpsilon

# Standard epsilon, the maximum relative precision of IEEE 754 double-precision floating numbers (64 bit).
# According to the definition of Prof. Higham and used in the ISO C standard and MATLAB.
POSITIVE_DOUBLE_PRECISION = Precision.PositiveDoublePrecision

# Actual double precision machine epsilon, the smallest number that can be added to 1, yielding a results different than 1.
# This is also known as unit roundoff error. According to the definition of Prof. Higham.
# On a standard machine this is equivalent to `PositiveDoublePrecision`.
POSITIVE_MACHINE_EPS = Precision.PositiveMachineEpsilon

# Standard epsilon, the maximum relative precision of IEEE 754 single-precision floating numbers (32 bit).
# According to the definition of Prof. Higham and used in the ISO C standard and MATLAB.
POSITIVE_SINGLE_PRECISION = Precision.PositiveSinglePrecision

# The number of significant decimal places of single-precision floating numbers (32 bit).
SINGLE_DECIMAL_PLACES = Precision.SingleDecimalPlaces

# Standard epsilon, the maximum relative precision of IEEE 754 single-precision floating numbers (32 bit).
# According to the definition of Prof. Demmel and used in LAPACK and Scilab.
SINGLE_PRECISION = Precision.SinglePrecision