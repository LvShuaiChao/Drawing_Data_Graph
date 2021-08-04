import matplotlib.pyplot as plt
import matplotlib.image as imgplt

img = imgplt.imread('1.jpg')
# plt.imshow(img)

plt.savefig('1_output.jpg')
plt.show()
