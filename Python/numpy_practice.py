import numpy as np


a = np.array([1,2,3])
print type(a)
print a.shape
print a[0], a[1], a[2]
a[0] = 5
print a


b = np.array([[1,2,3], [4,5,6]])
print type(b)
print b.shape
print b[0, 1], b[1, 1], b[0, 2]
print b


a = np.zeros((2,2))
print a

a = np.ones((2,2))
print a

a = np.full((2,2), 8)
print a


a = np.eye(2)
print a

a = np.random.random((2,2))
print a

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[:2, 1:3]
print b
print b.shape

a = np.array([[1,2], [3, 4], [5, 6]])
b = a[[0, 2, 1], [0, 1, 0]]
print b

a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a>2)
print bool_idx
print a[bool_idx]


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print x + y
print np.add(x, y)

x = np.array([[1,2],[3,4]])
v = np.array([9,10])
w = np.array([11, 12])
print v.dot(w)
print v.dot(x)
print x.dot(v)
print np.sum(x)
print np.sum(x, axis=0)
print np.sum(x, axis=1)


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)  # Create an empty matrix with the same shape as x
# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v
print y
vv = np.tile(v, (4, 1))
print vv
print x + vv




