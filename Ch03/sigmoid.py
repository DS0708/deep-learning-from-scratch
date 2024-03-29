import numpy as np
import matplotlib.pylab as plt
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# x = np.array([-1.0, 1.0, 2.0])
# print(sigmoid(x))
#
# x_graph = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x_graph)
# plt.plot(x_graph,y)
# plt.ylim(-0.1, 1.1) # y축 범위 지정
# plt.show()