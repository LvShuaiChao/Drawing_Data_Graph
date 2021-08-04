import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

x = [0, 3, 6, 9, 12, 15, 18, 21]
y = [1, 4, 7, 10, 13, 16, 19, 22]
z = [2, 5, 8, 11, 14, 17, 20, 23]

# 绘制散点图
fig = plt.figure()
ax = Axes3D(fig)
# ax.scatter(x, y, z,color="r",edgecolors='g')
ax.scatter(x, y, z,color="r")

# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('Z', fontdict={'size': 10, 'color': 'k'})
ax.set_ylabel('Y', fontdict={'size': 10, 'color': 'k'})
ax.set_xlabel('X', fontdict={'size': 10, 'color': 'k'})
plt.show()
