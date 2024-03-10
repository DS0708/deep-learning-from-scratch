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
# 2*2 행렬에 스칼라 값을 곱했을 때, 스칼라 값이 2*2행렬로 확대된 후 연산이 이루어지는데 이를 Broadast라고 한다
C = np.array([10,20])
print(A*C)  # A의 첫번쨰 column에는 10, 두번째 column에는 20이 곱해진다.

# 원소 접근
print(A)
print(A[0])
print(A[0][1])

for row in A:
    print(row)

# 1차원 배열로 변환
X = A.flatten()
print(X) #[1 2 3 4]
print(X[np.array([0,2])]) #[1 3], 인덱스가 0 2 인 원소 얻기
print(X>=3)     #[False False  True  True], 결과는 bool 배열
print(X[X>=3])  #[3 4], 인덱스가 3이상인 원소 얻기

'''
파이썬 같은 동적 언어는 C나 C++ 같은 정적 언어보다 처리 속도가 늦다.
그래서 빠른 성능이 요구될 경우 해당 부분을 C/C++로 구현한다.
그떄 파이썬은 C/C++로 쓰인 프로그램을 호출 하는 '중개자' 역할을 한다.
numpy도 주된 처리를 C와 C++로 구현하였기 때문에 성능을 해치지 않으면서 파이썬의 편리한 문법을 사용 가능하게 함
'''
