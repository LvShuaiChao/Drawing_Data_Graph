import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(1,20,20)
y = np.arange(10,30,1)
z = np.random.randint(20,50,20)  # numpy分别生成三个维度数据
fig = plt.figure()
ax = Axes3D(fig)  # 创建3D图的2种方式，第一种通过Axes3D将图片从二维变成三维，第二种通过在add_subplot(111,projection='3d'）将子图坐标修改成三维
ax.plot(x,y,z,'bo--')  # 参数与二维折现图不同的在于多了一个Z轴的数据
ax.set_zlabel('Z', fontdict={'size': 10, 'color': 'k'})
ax.set_ylabel('Y', fontdict={'size': 10, 'color': 'k'})
ax.set_xlabel('X', fontdict={'size': 10, 'color': 'k'})

plt.show()

