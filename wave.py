import numpy as np
import matplotlib.pyplot as plt


# var
L = 5
W = 5

# const var
pi = 3.1415926

# wave
A = 1
u = 343
v = 40000
_lambda = u / v
w = 2 * pi * v
T = 2 * pi / w
rho = 1.293


# y = Acos(wt-2pi(sqrt(x^2+y^2+z^2))/lambda)
# v = -Awsin(wt-2pi(sqrt(x^2+y^2+z^2))/lambda)
# a = -Aw^2cos(wt-2pi(sqrt(x^2+y^2+z^2))/lambda)
# r = sqrt(x^2+y^2+z^2)
# dv/dx = 2piAwcos(wt-2pi(r)/lambda)/lambda
# -dp/dx = rho(-Aw^2cos(wt-2pi(r)/lambda)-Awsin(wt-2pi(r)/lambda)*2piAwcos(wt-2pi(r)/lambda)/lambda)
#        = rho(-Aw^2cos(wt-2pi(r)/lambda)-piA^2*w^2sin(2wt-4pi(r)/lambda))
# integral by time(1T)
# -dp/dx = rho(-Awsin(wt-2pi(r)/lambda)+(1/2)*piA^2*wcos(2wt-4pi(r)/lambda))
#        = rho(-Awsin(-2pi(r)/lambda)+(1/2)*piA^2*wcos(4pi(r)/lambda)+Awsin(-2pi(r)/lambda)+piA^2*wcos(4pi(r)/lambda)/2)
#        = rho(piA^2*wcos(4pi(r)/lambda))
def wave_f(x1, y1, f):
    theta = 0
    for x, y in f.points:
        theta += np.cos(4 * pi * np.sqrt((x1 - x) ** 2 + (y1 - y) ** 2) / _lambda)
    return theta


# length
_l = L * _lambda / 2
_w = W * _lambda / 2

# degree
_N, _M = 100, 100


# be in real coordinate
def coordinate(x, y):
    x = x * _w / _N
    y = y * _l / _M
    return x, y


# create zero array
array = np.zeros((_N, _M))


# liner
# ax + by +c = 0
class F:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.points = []
        for i in range(_N):
            x, y = coordinate(i, 0)
            if b != 0:
                y = - self.c/self.b - self.a*x/self.b
            self.points.append([x, y])


# wave sounder
f0 = F(0, 1, 0)
f1 = F(0, 1, -_l)

# simulation
for i in range(_N):
    for j in range(_M):
        _x, _y = coordinate(i, j)
        array[j][i] = wave_f(_x, _y, f0)
        array[j][i] = wave_f(_x, _y, f1)

array = array * rho * (pi * A ** 2 * w)


contour = plt.contourf(array)

plt.colorbar(contour)

plt.show()
