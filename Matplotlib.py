import matplotlib.pyplot as plt
import Models

def Graph_1():
    data = Models.db.category_graph()
    x_lst = []
    y_lst = []
    for x,y in data:
        x_lst.append(y)
        y_lst.append(x)
    xpoints = x_lst
    ypoints = y_lst
    plt.bar(xpoints,ypoints)
    plt.show()