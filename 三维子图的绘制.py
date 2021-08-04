# -*- coding: utf-8 -*
# 载入模块
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 创建 1 张画布
fig = plt.figure()

#===============

# 向画布添加子图 1
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# 生成子图 1 数据
x = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
y = np.sin(x)
z = np.cos(x)

# 绘制第 1 张图
ax1.plot(x, y, z)

#===============

# 向画布添加子图 2
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# 生成子图 2 数据
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)

# 绘制第 2 张图
ax2.plot_surface(X, Y, Z, cmap=plt.cm.winter)

# 显示图
plt.show()
