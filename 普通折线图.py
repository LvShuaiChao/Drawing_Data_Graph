
def plot(x,y):
    from matplotlib import pyplot as plt #as就是重新命名的意思
    plt.figure()
    plt.plot(x,y)
    plt.title("title")
    plt.xlabel("x")
    plt.ylabel("y" )
    plt.show()


x = range(2, 26, 2)
y = [15,13,13.5,14,17,21,24,22,20,19,17,15]
plot(x,y)
