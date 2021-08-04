import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(100,500,(3,10,20))
x,y,z = data[0],data[1],data[2]  # numpy同时生成三维数据
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.plot_surface(x,y,z,cmap=plt.cm.winter,rstride=1,cstride=1) # rstride和cstride是隔几行几列取一个数字，代表曲面的稀疏度
plt.show()
