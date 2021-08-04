import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 10个点
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
# 每个点随机大小
s = (30 * np.random.rand(N)) ** 2
# 随机颜色
c = np.random.rand(N)
print(c)
print(type(c))
c = np.ones(10) * 0.01
c = [0.21474975, 0.50989718, 0.97118247, 0.94678956, 0.85493561, 0.66899823, 0.99432977, 0.09220956, 0.599639,
     0.73575595]
c =['r','r','r','r','r','r','r','r','r','r']
print(c)
print(type(c))

plt.scatter(x, y, s=s, c=c, alpha=0.5)
plt.show()
