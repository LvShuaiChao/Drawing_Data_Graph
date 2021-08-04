import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 计算x,y坐标对应的高度值
def f(x, y):
 return (1-x/2+x**5+y**3) * np.exp(-x**2-y**2)

# 生成x,y的数据
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值
X, Y = np.meshgrid(x, y)

# 填充等高线
plt.contourf(X, Y, f(X, Y), 20, cmap=plt.cm.hot)
# 添加等高线
C = plt.contour(X, Y, f(X, Y), 20)
plt.clabel(C, inline=True, fontsize=12)
# 显示图表
plt.show()
