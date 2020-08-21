import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation


# to get the distance of wave
# y = kx + b
# ax+by+cz+d = 0
class F:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def distance(self, x, y, z):
        return np.abs((self.a*x + self.b*y+self.c*z+self.d)/(np.sqrt(self.a**2+self.b**2+self.c**2)))


# become real axic
def axic(x, y, z):
    _x = x * _w / _N
    _y = y * _l / _M
    _z = z * _h / _O
    return _x, _y, _z


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
_N, _M, _O = 20, 20, 20

# create zero array
array = np.zeros((_N, _M, _O))

# length
_l = L * _lambda / 2
_w = L * _lambda / 2
_h = L * _lambda / 2

f1 = F(0, 0, 1, 0)
f2 = F(0, 0, 1, -_h)

for i in range(0, _N):
    for j in range(0, _M):
        for k in range(0, _O):
            _x, _y, _z = axic(i, j, k)
            array[i][j][k] = _pi * (f1.distance(_x, _y, _z)+_lambda/2-f2.distance(_x, _y, _z)) / _lambda

array = np.cos(array)

array = np.abs(array)

contour = plt.contourf(array[0, :, :])

plt.colorbar(contour)

plt.show()
