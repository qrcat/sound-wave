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
    for x, y, theta in points.points:
        ans1 += np.sin(w * times - k * (r(x, y, x1, y1)) + theta)
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


# 将曲线转换为各点坐标
class Point:
    def __init__(self):
        self.points = []
        self.len = 0

    def input(self, x, y, theta):
        self.points.append([x, y, theta])
        self.len += 1

    def cls(self):
        self.points = []
        self.len = 0


points = Point()


# 保存波源位置的函数
# theta 表示存在半个波程差

# 用于线性阵列的
# x = at + b
# y = ct + d
# e < t < f
class F:
    def __init__(self, a, b, c, d, e, f, theta=0):
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

theta0 = 0
theta1 = 0
theta2 = 0
theta3 = 0

road = [
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [-pi / 12, pi / 12, 0, 0],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],


    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [0, 0, -pi / 12, pi / 12],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [pi / 12, -pi / 12, 0, 0],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12],
    [0, 0, pi / 12, -pi / 12]
]


for sit in range(len(road)):
    # 用以保存速度均方之和的矩阵
    array_v_2 = np.zeros((_W, _L))

    # 初始化点
    points.cls()

    theta0 += road[sit][0]
    theta1 += road[sit][1]
    theta2 += road[sit][2]
    theta3 += road[sit][3]

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
    f0 = F(1, 0, 0, 0, _w / 4, 3 * _w / 4, theta0)
    f1 = F(1, 0, 0, _l, _w / 4, 3 * _w / 4, theta1)
    f3 = F(0, 0, 1, 0, _l / 4, 3 * _l / 4, theta2)
    f4 = F(0, _w, 1, 0, _l / 4, 3 * _l / 4, theta3)


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

    # 声势能的计算公式
    array_U = 2 * pi * (R**3) * (array_p_2_sqrt / (3 * rho * (u**2)) - rho * array_v_2 / 2)

    # 梯度的计算式
    array_grad = np.gradient(array_U)

    # 声势力

    plt.figure(figsize=(10, 10))

    plt.quiver(array_grad[0], array_grad[1])

    plt.title("Acoustic Potential Power")

    plt.text(1, 1, 'theta=U:{}'.format(sit))

    plt.savefig('{}.svg'.format(sit), dpi=600)
