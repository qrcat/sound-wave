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
def r(x0, y0, z0, x1=0, y1=0, z1=0):
    return np.sqrt(np.square(x0-x1) + np.square(y0-y1) + np.square(z0-z1))


# 波运算函数
def wave(x1, y1, z1, times):
    global array_v_2
    ans1 = 0
    for x, y, z, theta in points.points:
        ans1 += np.sin(w * times - k * (r(x, y, z, x1, y1, z1)) + z)
    array_v_2[j][i] += np.square(ans1)


# 长宽
L = 5
W = 5
H = 5
_l = L * _lambda / 2
_w = W * _lambda / 2
_h = H * _lambda / 2

# 精细化程度
# _L 用于切细x轴
# _W 用于切细y轴
# _H 用于切细z轴
_L, _W, _H, _Time_Split = 10, 10, 10, 10


# 由点转换为真实坐标
def coordinate(x, y, z):
    x = x * _w / _W
    y = y * _l / _L
    z = z * _H / _H
    return x, y, z


# 用以保存速度均方之和的矩阵
array_v_2 = np.zeros((_W, _L, _H))


# 将曲线转换为各点坐标
class Point:
    def __init__(self):
        self.points = []
        self.len = 0

    def input(self, x, y, z, theta):
        self.points.append([x, y, z, theta])
        self.len += 1


points = Point()


# 保存波源位置的函数
# theta 表示存在半个波程差

# a < x < b
# f1(x) < y < f2(x)
# z = f(x,y)
class F:
    def __init__(self, a, b, f1, f2, f, theta=0):
        mini_x = (b - a) / (_W + _L + _H)
        c, d = f1(a), f2(b)
        mini_y = (d - c) / (_W + _L + _H)
        for x_split in range(_W + _L + _H):
            x_i = mini_x * x_split
            for y_split in range(_W + _L + _H):
                y_i = mini_y * y_split
                z = f(x_i, y_i)
                points.input(x_i, y_i, z, theta)


# -1< x < 1
# -sqrt(1-x^2) < y < sqrt(1-x^2)
# z = 0

def f1(x):
    return np.sqrt(np.square(_lambda)-np.square(x))


def f2(x):
    return - np.sqrt(np.square(_lambda)-np.square(x))


def g1(x, y):
    return 0


def g2(x, y):
    return H*_lambda/2


F(-_lambda, _lambda, f1, f2, g1)
F(-_lambda, _lambda, f1, f2, g2)

# 模拟
split_time = T / _Time_Split
for t in range(_Time_Split):
    for i in range(_W):
        for j in range(_L):
            for k in range(_H):
                _x, _y, _z = coordinate(i, j, k)
                time = split_time * t
                wave(_x, _y, _z, time)


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

# 梯度的计算式
array_grad = np.gradient(array_U)

print(array_grad)


# 声压级
p_rms = 2e-5
array_level = 20 *np.log(np.abs(array_p_2_sqrt) / p_rms)

# 下面的函数均用于绘制图形
# 顺序是声压、声压级、声势能

# 声压

contour = plt.contourf(array_p_2_sqrt[_W//2, :, :])

plt.colorbar(contour)

plt.title("Sound Pressure")

plt.show()

# 声压级

contour = plt.contourf(array_level[_W//2, :, :])

plt.colorbar(contour)

plt.title("Sound Pressure Level")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

# 声势能

contour = plt.contourf(array_U[_W//2, :, :])

plt.colorbar(contour)

plt.title("Acoustic Potential Energy")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()

# 声势力

plt.quiver(array_grad[0], array_grad[1])

plt.title("Acoustic Potential Power")

plt.text(1, 1, 'L={}lambda/2,W={}lambda/2'.format(L, W))

plt.show()
