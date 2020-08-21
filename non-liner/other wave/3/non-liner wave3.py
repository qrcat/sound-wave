import numpy as np
import matplotlib.pyplot as plt

# var
L = 5
W = 5

# const var
pi = 3.1415926

# wave
A = 0.4
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
_N, _M = 50, 50


# be in real coordinate
def coordinate(x, y):
    x = x * _w / _N
    y = y * _l / _M
    return x, y


# create zero array
array = np.zeros((_N, _M))


# non-liner sounder
# x = at + b
# y = ct + d
# e < t < f
class F:
    def __init__(self, a, b, c, d, e, f):
        self.points = []
        divide = np.maximum(_M, _N)
        mini = (f - e) / divide
        for i in range(divide):
            t = mini * i + e
            self.points.append([a * t + b, c * t + d])


# wave sounder
# f0: x = -t
#     y = t
#     -_w/4<t<_w/4
# f1: x = t+_w
#     y = t
#     -_w/4<t<_w/4
f0 = F(-1, 0, 1, 0, -_w/4, _w/4)
f1 = F(1, _w, 1, 0, -_w/4, _w/4)

# simulation
for i in range(_N):
    for j in range(_M):
        _x, _y = coordinate(i, j)
        array[_M-j-1][_N-i-1] += wave_f(_x, _y, f0)/_M**2
        array[_M-j-1][_N-i-1] += wave_f(_x, _y, f1)/_N**2

array = array * rho * (pi * A ** 2 * w)

contour = plt.contourf(array)

plt.colorbar(contour)

plt.title("sound pressure")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()
