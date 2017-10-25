# new instance
>>> a = Mat3([
...     0.0, 2.0, 0.0,
...     0.0, 0.0, 1.0,
...     1.0, 0.0, 0.0,
... ])

>>> a
(0.0, 2.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0)

# transpose
>>> a.trans
(0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 0.0, 1.0, 0.0)

# determinant
>>> a.det
-2.0

# inverse
>>> a.inv
(0.0, -0.0, 1.0, 0.5, 0.0, -0.0, 0.0, 1.0, 0.0)

>>> b = Mat3([
...     1.0, 0.0, 0.0,
...     0.0, 2.0, 0.0,
...     0.0, 0.0, 3.0,
... ])

# matrix * matrix
>>> a * b
(0.0, 2.0, 0.0, 0.0, 0.0, 2.0, 3.0, 0.0, 0.0)

# matrix * vector
>>> v = Vec3([1.0, 0.0, 2.0])
>>> a * v
(2.0, 2.0, 0.0)

# matrix * float
>>> a * 2.5
(0.0, 5.0, 0.0, 0.0, 0.0, 2.5, 2.5, 0.0, 0.0)

# rows
>>> a.row(0)
(0.0, 0.0, 1.0)

# columns
>>> a.col(0)
(0.0, 2.0, 0.0)

# bytes
>>> bytes(a)
b'\x00\x00\x00\x00...\x00\x00\x00\x00'

# indexing
>>> a[6]
1.0

# new instance from a quaternion
>>> q = Quat([0.0, 0.0, 0.0, 1.0])
>>> m = Mat3(q)
>>> m
(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)