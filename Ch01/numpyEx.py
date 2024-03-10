import numpy as np

# numpy 배열 선언
x = np.array([1, 2, 3])
print(x)
print(type(x)) #<class 'numpy.ndarray'>

y = np.array([2,4,6])

# 원소끼리 연산
print(x+y)  #[3 6 9]
print(x*y)  #[ 2  8 18]
print(y/x)  #[2. 2. 2.]

print(y/2)  #[1. 2. 3.]

# 넘파이의 N차원 배열, 행렬
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)  #(2, 2), 2*2 Matrix라는 뜻, 차원을 묻는 함수 shape
print(A.dtype)  #int64, 담긴 자료형을 알 수 있음

B = np.array([[3,0],[0,6]])
print(A+B)  #shape가 같은 행렬끼리 덧셈 가능
print(A*B)  #차원이 유효현 행렬끼리 곱셈 가능

# 브로드캐스트


