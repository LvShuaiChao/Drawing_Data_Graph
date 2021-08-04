import matplotlib.pyplot as plt

img = plt.imread('1.jpg')
img_s = img[:,:,0]# 直接读入的img为3通道，这里用直接赋值的方法转为单通道
sc = plt.imshow(img_s)
sc.set_cmap('hot')# 这里可以设置多种模式
# plt.colorbar()# 显示色度条


plot = plt.gca()

frame = plt.gca()
# y 轴不可见
frame.axes.get_yaxis().set_visible(False)
# x 轴不可见
frame.axes.get_xaxis().set_visible(False)
frame.spines['top'].set_visible(False)
frame.spines['right'].set_visible(False)
frame.spines['bottom'].set_visible(False)
frame.spines['left'].set_visible(False)

plt.savefig('hah.png', bbox_inches='tight', dpi=500, pad_inches=0.0)
