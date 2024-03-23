import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=int)

x = np.array([-1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
y = step_function(x)
print(y)

x_graph = np.arange(-5.0, 5.0, 0.1)
y = step_function(x_graph)
plt.plot(x_graph,y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()
