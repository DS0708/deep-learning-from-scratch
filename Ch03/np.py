import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.dot(A,B)
print(C)

D = np.array([3,4])
print(np.dot(A,D))

X = np.array([1,2])
W = np.array([[1,3,5],[2,4,6]])
Y = np.dot(X,W)
print(Y)

Q = np.array([[1,2],[1,2],[0,1]])
print(Q.shape)

Z = np.array([1,1])
print(Z.shape)

print(np.dot(Q,Z))

