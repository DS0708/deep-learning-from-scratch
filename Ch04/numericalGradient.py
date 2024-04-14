import numpy as np

def numerical_gradient(f,x):
    h = 1e-4 # 0.001
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp = x[idx]
        # f(x+h) 계산
        x[idx] = tmp + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp

    return grad

def function1(x) :
    return x[0]**2 + x[1]**2

x = np.array([3.0, 4.0])

print(numerical_gradient(function1,x))
