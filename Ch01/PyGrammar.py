# 산술 연산
print(1-2)
print(4*5)
print(7/5)  # 1.4, 파이썬2 에서는 결과가 1 이다.
print(3**2) # 9

# 자료형
print(type(10))
print(type(2.718))
print(type("hello"))
hungry = True
sleepy = False
print(type(hungry)) #<class 'bool'>
print(hungry and sleepy) # False
print(hungry or sleepy) # True

# 변수
x = 10
y = 3.14
print(x)
print(x*y)
print(type(x*y))    # <class 'float'>

# 리스트
a = [1,2,3,4,5]
print(a)
print(len(a))
print(a[0])
print(a[4])
a[4] = 99
print(a)

# 리스트 Slicing(슬라이싱)
print(a[0:2])   # 인덱스 0부터 2까지 얻기 (2는 포함하지 않음)
print(a[1:])    # 인덱스 1부터 끝까지
print(a[:3])    # 인덱스 처음부터 3까지 (3은 미포함)
print(a[:-1])   # 인덱스 처음부터 마지막 원소의 1개 앞까지 얻기
print(a[:-2])   # 인덱스 처음부터 마지막 원소의 2개 앞까지 얻기

# 딕셔너리
me = {'height' : 180}   # 딕셔너리 생성
print(me['height'])     # 키 값을 이용하여 원소에 접근
me['weight'] = 70       # 새 원소 추가
print(me)               # 딕셔너리 출력, {'height': 180, 'weight': 70}

# if
if hungry:
    print("I'm hungry")
else :
    print("I'm not hungry")

# for
for i in [1,2,3]:
    print(i)

# Function
def hello(obj):
    print("Hello",obj)
hello("DS")

