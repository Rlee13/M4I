# M4I

IronPython interface classes to MathNet.Numerics. The intention is to quickly port numpy matrices to IronPython (and allow the use of python slices objects).

Implements (among others) 3x3 Matrix (MatrixD3), 4x4 Matrix (MatrixD4) and m x n Matrix (MatrixDMN).
Allows working with python's slice objects, i.e. one can do 

```python
print(S[1:2, 1:2])
```
to print the content of matrix S between row 1 and 2 and column 1 and 2.

For a gain in speed use MathNet.Numerics classes directly.

For usage, see the examples provided.

M4I is currently in an Alpha state of development.

# References

MathNet.Numerics

-- https://numerics.mathdotnet.com/
