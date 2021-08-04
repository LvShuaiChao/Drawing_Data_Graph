import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def hist1():
    # 设置matplotlib正常显示中文和负号
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']    # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    data = np.random.randn(10000)
    '''
    data: 绘图数据
    bins：直方图的长方形数目， 可选项， 默认为10
    normed：是否将得到的直方图向量归一化， 可选项， 默认为0， 代表不归一化， 显示频数。 normed=1，表示归一化，显示频率
    facecolor: 长方形的颜色
    edgecolor： 长方形边框的颜色
    alpha： 透明度
    '''
    # plt.hist(data, bins=40, density=1, facecolor='blue', edgecolor='black', alpha=0.7)
    plt.hist(data, bins=40, density=1, edgecolor='black', alpha=0.7)
    # 显示横轴标签
    plt.xlabel("区间")
    # 显示纵轴标签
    plt.ylabel("频数/频率")
    # 显示图标数
    plt.title("频数/频率分布直方图")
    plt.show()


if __name__ == '__main__':
    hist1()
