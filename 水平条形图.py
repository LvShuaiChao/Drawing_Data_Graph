def bar_graph_plot(data,labels,xlabel='x',title='title'):       #
    '''需要输入的为对应的很坐标的值，'''
    #各个条形图的名称
    #具体的坐标的值
    #标题的值
    #横坐标轴的名称
    #纵坐标轴的名称

    import matplotlib.pyplot as plt
    import matplotlib

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    """
    绘制水平条形图方法barh
    参数一：y轴
    参数二：x轴
    """
    plt.barh(range(len(data)), data, height=0.7, color='steelblue', alpha=0.8)      # 从下往上画
    plt.yticks(range(len(data)), labels)
    plt.xlim(min(data)/1.1, max(data) * 1.05)
    plt.xlabel(xlabel)
    plt.title(title)
    for x, y in enumerate(data):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    plt.show()

data = [39.5, 39.9, 45.4, 38.9, 40.1]
labels = ['亚马逊', '当当网', '中国图书网', '京东', '天猫']

bar_graph_plot(data=data, labels=labels,title='标题',xlabel='价格')
