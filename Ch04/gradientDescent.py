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

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad

    return x

def func(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0,4.0])
print(gradient_descent(func,init_x=init_x,lr=1e-10,step_num=100))
