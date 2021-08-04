import matplotlib.pyplot as plt
import numpy as np
# 10个点
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
# 每个点随机大小
s = (30*np.random.rand(N))**2
plt.scatter(x, y, s=100)
plt.show()
