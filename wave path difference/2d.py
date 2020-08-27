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

# const var
_pi = 3.1415926

# wave
_u = 343
_v = 40000
_lambda = _u / _v
_w = 2*_pi*_v

# degree
_N, _M = 200, 200

# create zero array
array = np.zeros((_N, _M))

# length
_l = L * _lambda / 2
_w = L * _lambda / 2

f1 = F(0, 1, 0)
f2 = F(0, 1, -_l)

for i in range(0, _N):
    for j in range(0, _M):
        _x, _y = axic(i, j)
        array[j][i] = _pi * (f1.distance(_x, _y)+_lambda/2-f2.distance(_x, _y)) / _lambda

array = np.cos(array)

array = np.abs(array)

contour = plt.contourf(array)

plt.colorbar(contour)

plt.show()
