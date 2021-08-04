from PIL import Image
import numpy as np
import 绘图.pyplot as plt

src = Image.open('1.jpg')
r, g, b = src.split()

plt.figure("lena")
ar = np.array(r).flatten()
plt.hist(ar, bins=256, stacked=True, facecolor='r', edgecolor='r')
ag = np.array(g).flatten()
plt.hist(ag, bins=256, stacked=True, facecolor='g', edgecolor='g')
ab = np.array(b).flatten()
plt.hist(ab, bins=256, stacked=True, facecolor='b', edgecolor='b')
plt.show()
