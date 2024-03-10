import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


# 단순한 그래프 그리기

## data init
x = np.arange(0,6,0.1)  # 0에서 6까지 0.1간격으로 생성, [0, 0.1, 0.2, ... 5.8, 5.9]라는 데이터 생성
y = np.sin(x)

## make a graph
plt.plot(x,y)
plt.show()


# pyplot의 기능

## data init
y1 = np.sin(x)
y2 = np.cos(x)

## make a graph
plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos") # cos 함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title('sin & cos') # 제목
plt.legend()    # 어떤 선이 어떤 그래프인지 나타내줌, 왼쪽 하단에
plt.show()


# 이미지 표시하기
img = imread('../dataset/cactus.png')
plt.imshow(img)
plt.show()
