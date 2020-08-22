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


# 波动方程需要改写
def wave_f(x1, y1, p):
    theta = 0
    for x, y in p.points:
        for x0, y0 in p.points:
            theta += np.cos(2 * k * (r(x0, y0, x1, y1) - r(x, y, x1, y1)))
    return theta


# length
_l = L * _lambda / 2
_w = W * _lambda / 2

# degree
_N, _M = 20, 20


# be in real coordinate
def coordinate(x, y):
    x = x * _w / _M
    y = y * _l / _N
    return x, y


# create zero array
array = np.zeros((_M, _N))


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
#     0<t<_w/3
# f1: x = t
#     y = -lambda/4
#     _w/3<t<2_w/3
# f2: x = t
#     y = 0
#     2_w/3<t<_w/3
# f3: x = t
#     y = l
#     -<t<_w/3
# f4: x = t
#     y = l+lambda/4
#     _w/3<t<2_w/3
# f5: x = t
#     y = l
#     2_w/3<t<3_w/3
fi = _lambda/2

f0 = F(1, 0, 0, 0, 0, _w/3)
f1 = F(1, 0, 0, fi, _w/3, 2*_w/3)
f2 = F(1, 0, 0, 0, 2*_w/3, _w)
f3 = F(1, 0, 0, _l, 0, _w/3)
f4 = F(1, 0, 0, _l-fi, _w/3, 2*_w/3)
f5 = F(1, 0, 0, _l, 2*_w/3, _w)

# simulation
for i in range(_N):
    for j in range(_M):
        _x, _y = coordinate(i, j)
        array[j][i] += wave_f(_x, _y, points)



# 声压

array1 = 4*w*rho*pi**2*(A/points.len)**2*array

contour = plt.contourf(array1)

plt.colorbar(contour)

plt.title("sound pressure")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

# 声压级

p_rms = 2e-5

array2 = np.abs(array)/p_rms

array2 = 20 * np.log(array2)

contour = plt.contourf(array2)

plt.colorbar(contour)

plt.title("sound level")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()


# 声势

R = 1

array3 = 2 * pi * R**3 * (np.abs(array1)/(3*rho*u**2)-2*pi*w*rho*(A/points.len)**2*v_2)


contour = plt.contourf(array3)

plt.colorbar(contour)

plt.title("sound U")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()