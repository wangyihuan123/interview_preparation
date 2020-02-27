import numpy as np

a1x3 = np.array([1, 2, 3], ndmin=2)
a1x4 = np.array([1, 2, 3, 4], ndmin=2)
b3x1 = np.array([[1], [2], [3]], ndmin=2)
c1x9 = np.array(np.arange(9), ndmin=2)
d3x4 = np.ones((3,4))
print("a1x3", a1x3.shape, a1x3)
print("b3x1", b3x1.shape, b3x1)
# print(c1x9.shape, c1x9)
print(d3x4.shape, d3x4)
print("===================")
print(b3x1*d3x4, (b3x1 * d3x4).shape)
print(d3x4*b3x1, (d3x4 * b3x1).shape)

print("-------------")
# print(a1x3*d3x4, (a1x3 * d3x4).shape)
# print(d3x4*a1x3, (d3x4*a1x3).shape)
print(a1x3 * b3x1)

