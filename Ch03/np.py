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

X2 = np.array([[1],[2]])
X3 = np.array([1,2])

print("-----------------")
print(X.shape)
print(X2.shape)
print(X3.shape)
print(W.shape)
XX2 = np.dot(X,X2)
XX3 = np.dot(X,X3)
print(XX2.shape)
print(XX3.shape)
print(XX3)
print("-----------------")

print(Y)

Q = np.array([[1,2],[1,2],[0,1]])
print(Q.shape)

Z = np.array([1,1])
print(Z.shape)

print(np.dot(Q,Z))



