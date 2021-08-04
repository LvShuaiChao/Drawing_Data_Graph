from PIL import Image
import numpy as np
import 绘图.pyplot as plt
img=np.array(Image.open('1.jpg').convert('L'))

plt.figure("lena")
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256, stacked=True, facecolor='green', alpha=0.75)
plt.show()
