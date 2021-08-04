import matplotlib.pyplot as plt
def vertical_bar_graph_plot(data,label,color='b'):

    plt.bar(data[0],data[1], label=label,color=color)
    plt.legend()
    plt.xlabel('bar number')
    plt.ylabel('bar height')

    plt.title('Epic Graph\nAnother Line! Whoa')


#第一个位置存放的是横坐标，第二个位置存放的是纵坐标
data1 = [[1,3,5,7,9],[5,2,7,8,2]]
data2 = [[2,4,6,8,10],[8,6,2,5,6]]

vertical_bar_graph_plot(data1,'Example One','b')
vertical_bar_graph_plot(data2,'Example Two','g')
plt.show()
