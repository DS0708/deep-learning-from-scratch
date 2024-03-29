import numpy as np
from sigmoid import sigmoid

def identity_fun(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.1, 0.1], [0.5, 0.1, 0.1]])
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.2, 0.1], [0.5, 0.8], [0.4, 0.3]])
    network['B2'] = np.array([0.1, 0.1])
    network['W3'] = np.array([[0.1,0.2],[0.3,0.4]])
    network['B3'] = np.array([0.1,0.4])
    return network

def forward(network, X) :
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['B1'], network['B2'], network['B3']

    A1 = np.dot(X,W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1,W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2,W3) + B3
    y = identity_fun(A3)

    return y

network = init_network()
X = np.array([0.5, 0.4])
y = forward(network, X)
print(y)

