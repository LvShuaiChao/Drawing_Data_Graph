import matplotlib.pyplot as plt
value_x = list(range(1, 50))
value_y = [v**2  for v in value_x]
plt.scatter(value_x, value_y, c=value_y, cmap=plt.cm.Blues, s=40)
#如果想取消点的边缘颜色，上面有介绍
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(labelsize=14)
plt.show()

