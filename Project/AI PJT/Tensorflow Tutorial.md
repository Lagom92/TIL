# Tensorflow Tutorial

- Tensorflow 공식 사이트

  ​	- 튜토리얼 - 분류 문제_[링크](https://www.tensorflow.org/tutorials/keras/basic_classification)





## 옷 이미지를 분류하는 신경망 모델 훈련을 해보자.



- tensorflow와 [keras](https://www.tensorflow.org/guide/keras)를 임포트한다.

```
import tensorflow as tf
from tensorflow import keras

# Tensorflow version: 1.14.0
```



- 헬퍼(helper) 라이브러리를 임포트한다.

```
import numpy as np
import matplotlib.pyplot as plt
```





### 패션 MNIST 데이터셋 임포트하기

- 사용하는 데이터셋: 패션 MNIST_[링크](https://github.com/zalandoresearch/fashion-mnist)



- 훈련 데이터와 테스트 데이터로 데이터셋 나누기

```
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```



- 데이터셋에 클래스 이름(옷이나 물건 이름)이 없으므로 별도로 변수를 만들어 준다.

```
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
```



- 이미지의 개수와 픽셀 확인하기

```
train_images.shape

# (60000, 28, 28)
# 60000개의 이미지, 28x28 픽셀
```



- 0번째 이미지 확인하기

```
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
```



- 정규화 하기
- 0 ~ 255까지인 픽셀 범위를 0 ~ 1로 변경하기

```
train_images = train_images / 255.0

test_images = test_images / 255.0
```







### 모델 구성



#### 층 설정

- 

```
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
```



- `tf.keras.layers.Flatten`은 2차원 배열을 1차원 배열로 변환 시킨다.



- `tf.keras.layers.Dense`는 밀집 연결(densely connected) 또는 완전 연결(fully connected)층이라고 부른다.
- 첫번재 dense층은 128개의 노드를 가진다.
- 마지막 dense층은 10개의 노드의 softmax 층이다.이 층은 10개의 확률을 반환하고 반환된 값의 전체 합은 1이다. 
- 각 노드는 현재 이미지가 10개 클래스 중 하나에 속할 확률을 출력한다.



#### 모델 컴파일

- 손실함수(Loss Function): 훈련 하는 동안 모델의 오차를 측정한다. 모델의 학습이 올바른 방향으로 향하도록 이 함수를 최소화 해야 한다.
- 옵티마이저(Optimizer): 데이터와 손실 함수를 바탕으로 모델의 업데이트 방법을 결정한다.
- 지표(Metrics):  훈련 단계와 테스트 단계를 모니터링하기 위해 사용한다. (ex) 정확도)



```
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```





#### 모델 훈련

신경망 모델을 훈련하는 단계

- 훈련 데이터를 모델에 넣는다.
- 모델이 이미지와 레이블을 매핑하는 방법을 배운다.
- 테스트 세트에 대한 모델의 예측을 만든다.



- 모델이 훈련 데이터를 학습한다.

```
model.fit(train_images, train_labels, epochs=10)
```

모델이 훈련되면서 손실(loss)와 정확도(acc)를 출력한다.





#### 정확도 평가

```
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('테스트 정확도:', test_acc)
```





....to be continue