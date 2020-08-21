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
# v = -Awsin^2(wt-2pi(sqrt(x^2+y^2+z^2))/lambda)
#     cos 2x = (cos x)^2 - (sin x)^2 = 1 - 2(sin x)^2
#     (sin x)^2 = (1 - cos 2x)/2
#     v^2 = Aw(1-cos(2wt - 4pi(r)/lambda)/2
# integral v^2 by time
#     @v^2 = (1/2)AwT - Awsin(4pi-4pi(r)/lambda)/4 + Awsin(-4pi(r)/lambda)/4
#          = (1/2)AwT + Awsin(4pi(r)/lambda)/4 - Awsin(4pi(r)/lambda)/4
#          = (1/2)AwT
# a = -Aw^2cos(wt-2pi(sqrt(x^2+y^2+z^2))/lambda)
#      r = sqrt(x^2+y^2+z^2)
# dv/dx = 2piAwcos(wt-2pi(r)/lambda)/lambda
# -dp/dx = rho(-Aw^2cos(wt-2pi(r)/lambda)-Awsin(wt-2pi(r)/lambda)*2piAwcos(wt-2pi(r)/lambda)/lambda)
#        = rho(-Aw^2cos(wt-2pi(r)/lambda)-piA^2*w^2sin(2wt-4pi(r)/lambda))
# integral by time(1T)
# @-dp/dx = rho(-Awsin(wt-2pi(r)/lambda)+(1/2)*piA^2*wcos(2wt-4pi(r)/lambda))
#         = rho(-Awsin(-2pi(r)/lambda)+(1/2)*piA^2*wcos(4pi(r)/lambda)+Awsin(-2pi(r)/lambda)+piA^2*wcos(4pi(r)/lambda)/2)
#         = rho(piA^2*wcos(4pi(r)/lambda))
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
array_v = np.zeros((_N, _M))

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
# f0: x = t
#     y = 0
#     _w/4<t<3_w/4
# f1: x = t
#     y = l
#     _w/4<t<3_w/4
# f3: x = 0
#     y = t
#     _l/4<t<3_l/4
# f4: x = _w
#     y = t
#     _l/4<t<3_l/4
f0 = F(1, 0, 0, 0, _w/4, 3*_w/4)
f1 = F(1, 0, 0, _l, _w/4, 3*_w/4)
f3 = F(0, 0, 1, 0, _l/4, 3*_l/4)
f4 = F(0, _w, 1, 0, _l/4, 3*_l/4)

# simulation
for i in range(_N):
    for j in range(_M):
        _x, _y = coordinate(i, j)
        array[j][i] += wave_f(_x, _y, f0)/_M**2
        array[j][i] += wave_f(_x, _y, f1)/_N**2
        array[j][i] += wave_f(_x, _y, f3)/_M**2
        array[j][i] += wave_f(_x, _y, f4)/_N**2

array = array * rho * (pi * A ** 2 * w)


# U = 2 * pi * R^3 (_p/3rhoc^2 - rho*v^2/2)
array = 2 * pi * (array/(3*rho*u**2)-rho*0.5*A*w*T/2)


contour = plt.contourf(array)

plt.colorbar(contour)

plt.title("sound U")

plt.show()
