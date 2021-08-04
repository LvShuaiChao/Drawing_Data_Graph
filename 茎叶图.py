import matplotlib.pyplot as plt
import numpy as np

# 构造数据
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))


# 演示默认参数、默认样式
plt.subplot(221)
plt.stem(y)
# 演示茎线、茎头、基线样式
plt.subplot(222)
plt.stem(x, y, linefmt='r--', markerfmt='gD', basefmt='b--', bottom=1)
# 演示水平茎叶图
plt.subplot(223)
plt.stem(x, y, orientation='horizontal')
# 演示stem返回值
plt.subplot(224)
markerline, stemlines, baseline = plt.stem(x, y)
print(markerline.get_color(),  baseline.get_color())
plt.show()
