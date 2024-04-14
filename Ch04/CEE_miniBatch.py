import numpy as np

def cross_entropy_error(y,t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = t.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7))/batch_size


# t가 원-핫 인코딩 방식으로 주어지지 않을 떄

def cross_entropy_error_noOneHot(y,t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = t.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum( np.log(y[np.arange(batch_size),t] + 1e-7) ) / batch_size