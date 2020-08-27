import numpy as np
import matplotlib.pyplot as plt

# to get the distance of wave
# y = kx + b
# ax+by+c = 0
class F:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def distance(self, x, y):
        return np.abs((self.a*x + self.b*y+self.c)/(np.sqrt(self.b**2+self.a**2)))

# become real axic
def axic(x, y):
    _x = x * _w / _N
    _y = y * _l / _M
    return _x, _y


# var
L = 9
W = 9

# const var
_pi = 3.1415926

# wave
_u = 343
_v = 40000
_lambda = _u / _v
_w = 2*_pi*_v

# degree
_N, _M = 20, 20

# create zero array
array = np.zeros((_N, _M))

# length
_l = L * _lambda / 2
_w = W * _lambda / 2

f1 = F(1, 1, 0)
f2 = F(-1, 1, _w)

for i in range(_N):
    for j in range(_M):
        _x, _y = axic(i, j)
        array[j][i] += np.cos(_pi * ((f1.distance(_x, _y)-f2.distance(_x, _y))/_lambda))

array = np.abs(array)

contour = plt.contourf(array)

plt.colorbar(contour)

plt.show()
