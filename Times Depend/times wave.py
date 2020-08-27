import numpy as np
import matplotlib.pyplot as plt


# 常量
pi = 3.1415926

# 声波属性
A = 0.01
u = 343
v = 40000
_lambda = u / v
w = 2 * pi * v
k = 2 * pi / _lambda
T = 2 * pi / w
rho = 1.293

# 悬浮物件的尺度
R = 0.005


# 两点换算为距离
def r(x0, y0, x1=0, y1=0):
    return np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


# 波运算函数
def wave(x1, y1, times):
    global array_v_2
    ans1 = 0
    for x, y, z in points.points:
        if z:
            z = pi
        ans1 += np.sin(w * times - k * (r(x, y, x1, y1)) + z)
    array_v_2[j][i] += np.square(ans1)


# 长宽
L = 5
W = 5
_l = L * _lambda / 2
_w = W * _lambda / 2

# 精细化程度
# _L 用于切细横坐标
# _W 用于切细纵坐标
_L, _W, _Time_Split = 50, 50, 50


# 由点转换为真实坐标
def coordinate(x, y):
    x = x * _w / _W
    y = y * _l / _L
    return x, y


# 用以保存速度均方之和的矩阵
array_v_2 = np.zeros((_W, _L))


# 将曲线转换为各点坐标
class Point:
    def __init__(self):
        self.points = []
        self.len = 0

    def input(self, x, y, theta):
        self.points.append([x, y, theta])
        self.len += 1


points = Point()


# 保存波源位置的函数
# theta 表示存在半个波程差

# 用于线性阵列的
# x = at + b
# y = ct + d
# e < t < f
class F:
    def __init__(self, a, b, c, d, e, f, theta=False):
        mini = (f - e) / (_W + _L)
        for t_split in range(_W + _L):
            t_i = mini * t_split + e
            points.input(a * t_i + b, c * t_i + d, theta)


# 用于圆周阵列的
# x = a*cos(t) + b
# y = c*sin(t) + d
# e < t < f
class FCircle:
    def __init__(self, a, b, c, d, e, f, theta = False):
        self.points = []
        mini = (f - e) / (_W + _L)
        for t_split in range(_W + _L):
            t_i = mini * t_split + e
            points.input(a * np.cos(t_i) + b, c * np.sin(t_i) + d, theta)

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
split_time = T / _Time_Split
for t in range(_Time_Split):
    for i in range(_W):
        for j in range(_L):
            _x, _y = coordinate(i, j)
            time = split_time * t
            wave(_x, _y, time)


# 将矩阵乘以系数
array_v_2 = A ** 2 * w ** 2 * array_v_2 / (points.len + 1)**2
array_p_2 = rho**2 * u**2 * k**2 * array_v_2
array_v_2 /= _Time_Split
array_p_2 /= _Time_Split
array_p_2_sqrt = np.sqrt(array_p_2)


def potential_energy(p, v_):
    return


# 声势能的计算公式
array_U = 2 * pi * (R**3) * (array_p_2_sqrt / (3 * rho * (u**2)) - rho * array_v_2 / 2)

# 声压级
p_rms = 2e-5
array_level = 20 *np.log(np.abs(array_p_2_sqrt) / p_rms)

# 下面的函数均用于绘制图形
# 顺序是声压、声压级、声势能

# 声压

contour = plt.contourf(array_p_2_sqrt)

plt.colorbar(contour)

plt.title("Sound Pressure")

plt.show()

# 声压级

contour = plt.contourf(array_level)

plt.colorbar(contour)

plt.title("Sound Pressure Level")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

# 声势能

contour = plt.contourf(array_U)

plt.colorbar(contour)

plt.title("Acoustic Potential Energy")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()
