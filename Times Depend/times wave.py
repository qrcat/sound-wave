import numpy as np
import matplotlib.pyplot as plt

# var
L = 5
W = 5

# 常量
pi = 3.1415926

# 声波属性
A = 0.001
u = 343
v = 40000
_lambda = u / v
w = 2 * pi * v
k = 2 * pi / _lambda
T = 2 * pi / w
rho = 1.293


# 换算为距离
def r(x0, y0, x1=0, y1=0):
    return np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


def wave_f(x1, y1, times):
    global array_v, array_v_2
    ans0, ans1 = wave(x1, y1, times, points)
    array_v[j][i] += ans0
    array_v_2[j][i] += ans1


# depend on time
def wave(x1, y1, time, p):
    ans1 = 0
    for x, y, z in p.points:
        if z:
            z = pi
        ans1 += np.sin(w * time - k * (r(x, y, x1, y1)) + z)
    return ans1, ans1**2


# 长宽
_l = L * _lambda / 2
_w = W * _lambda / 2

# 精细化程度
_N, _M, _T_split = 50, 50, 50


# 转换为真实坐标
def coordinate(x, y):
    x = x * _w / _M
    y = y * _l / _N
    return x, y


# 保存各点属性
array_v = np.zeros((_M, _N))
array_v_2 = np.zeros((_M, _N))


# 将曲线转换为各点坐标
class Point:
    def __init__(self):
        self.points = []
        self.len = 0

    def input(self, x, y, theta):
        self.points.append([x, y, theta])
        self.len += 1


points = Point()


# theta 表示存在半个波程差

# 用于线性阵列的
# x = at + b
# y = ct + d
# e < t < f
class F:
    def __init__(self, a, b, c, d, e, f, theta=False):
        divide = np.maximum(_M, _N)
        mini = (f - e) / divide
        for i in range(divide):
            t = mini * i + e
            points.input(a * t + b, c * t + d, theta)


# 用于圆周阵列的
# x = a*cos(t) + b
# y = c*sin(t) + d
# e < t < f
class FCircle:
    def __init__(self, a, b, c, d, e, f, theta = False):
        self.points = []
        divide = np.maximum(_M, _N)
        mini = (f - e) / divide
        for i in range(divide):
            t = mini * i + e
            points.input(a * np.cos(t) + b, c * np.sin(t) + d, theta)

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

# 模拟
split_time = T / _T_split
for t in range(_T_split):
    for i in range(_M):
        for j in range(_N):
            _x, _y = coordinate(i, j)
            time = split_time * t
            wave_f(_x, _y, time)

array_v = array_v * (A * w / (points.len + 1) )
array_v_2 = array_v_2 * (A ** 2 * w ** 2 / (points.len + 1)**2) / _T_split
array_p_2 = rho**2 * u**2 * k**2 * array_v_2
array_p_2_sqrt = np.sqrt(array_p_2)

U = 2 * pi * 1 ** 3 * (array_p_2_sqrt / (3 * rho * u ** 2) - rho * array_v_2 / 2)

contour = plt.contourf(U)

plt.colorbar(contour)

plt.title("声势能")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

# 声压级

p_rms = 2e-5

array_level = np.abs(array_p_2_sqrt) / p_rms

array_level = 20 * np.log(array_level)

contour = plt.contourf(array_level)


plt.colorbar(contour)

plt.title("声压级")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()
