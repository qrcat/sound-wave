import numpy as np
import matplotlib.pyplot as plt

# var
L = 5
W = 5

# const var
pi = 3.1415926

# wave
A = 0.6
u = 343
v = 40000
_lambda = u / v
w = 2 * pi * v
k = 2 * pi / _lambda
T = 2 * pi / w
rho = 1.293


# translate into real distance
def r(x0, y0, x1=0, y1=0):
    return np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


# depend on time
def wave_f(x1, y1, time,p):
    theta = 0
    for x, y in p.points:
        theta += np.cos(w*time - k * (r(x, y, x1, y1)))
    return theta


# length
_l = L * _lambda / 2
_w = W * _lambda / 2

# degree
_N, _M, _T_split = 25, 25, 25


# be in real coordinate
def coordinate(x, y):
    x = x * _w / _M
    y = y * _l / _N
    return x, y


# create zero array
array = np.zeros((_M, _N))
array_y = np.zeros((_M, _N))
array_y_Last = np.zeros((_M, _N))
array_v = np.zeros((_M, _N))
array_v_Last = np.zeros((_M, _N))
array_v_2 = np.zeros((_M, _N))
array_a = np.zeros((_M, _N))
array_p = np.zeros((_M, _N))

# use point to all the F point
class Point:
    def __init__(self):
        self.points = []
        self.len = 0

    def input(self, x, y):
        self.points.append([x, y])
        self.len += 1


points = Point()


# non-liner sounder
# x = at + b
# y = ct + d
# e < t < f
class F:
    def __init__(self, a, b, c, d, e, f):
        divide = np.maximum(_M, _N)
        mini = (f - e) / divide
        for i in range(divide):
            t = mini * i + e
            points.input(a * t + b, c * t + d)


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
split_time = T / _T_split
for t in range(_T_split):
    time = t*split_time
    array_y_Last = array_y
    array_v_Last = array_v
    for i in range(_M):
        for j in range(_N):
            _x, _y = coordinate(i, j)
            array_y[j][i] = wave_f(_x, _y, time,points)
    array = array_y + array_y_Last
    array_v = (array_y - array_y_Last)/(T/_T_split)
    array_v_2 = np.square(array_v)/(T/_T_split)
    array_a = (array_v - array_v_Last) / (T / _T_split)

array_y *= (A/points.len)
array_v *= (A/points.len)
array_p *= (A/points.len)
array_a *= (A/points.len)

# 声压

array_p = rho * (array_a + array_v*array_v)

contour = plt.contourf(array_p)

plt.colorbar(contour)

plt.title("sound pressure")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

# 声压级

p_rms = 2e-5

array2 = np.abs(array) / p_rms

array2 = 20 * np.log(array2)

contour = plt.contourf(array2)

plt.colorbar(contour)

plt.title("sound level")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

