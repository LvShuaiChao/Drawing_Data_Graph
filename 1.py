import matplotlib.pyplot as plt
import matplotlib.image as imgplt
x = imgplt.imread('1.jpg')

plt.imshow(x)

frame = plt.gca()
# y 轴不可见
frame.axes.get_yaxis().set_visible(False)
# x 轴不可见
frame.axes.get_xaxis().set_visible(False)
frame.spines['top'].set_visible(False)
frame.spines['right'].set_visible(False)
frame.spines['bottom'].set_visible(False)
frame.spines['left'].set_visible(False)
plt.show()


plt.waitforbuttonpress(0)