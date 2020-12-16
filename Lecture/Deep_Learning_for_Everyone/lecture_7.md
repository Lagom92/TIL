# Lecture 07-1 

## Application & Tips: Learning rate, data preprocessing, overfitting



<br/>

### Large learning rate

- overshooting
- lr이 너무 크면 발생함



<br/>

### Small learning rate

- takes too long, stops at local minimum
- lr이 너무 작으면 발생



<br/>

![](./img/learning_rate.png)



<br/>

즉, learning rate 를 정확학 값을 찾아야 한다

일반척으로 맨처음에는 0.01 로 시작



<br/>

### data preprocessing for gradient descent

- zero-centered data
- normalized data



<br/>

### Standardization



<br/>

### Overfitting

- 학습 데이터에 너무 맞는 모델
- 테스트 데이터나 실제 데이터에는 맞지 않음



<br/>

overfitting 해결법

- more training data
- reduce the number of features
- Regularization





<br/>

<br/>

# Lecture 07-2

## Application & Tips: Learning and test data sets



<br/>

AI model 평가 



<br/>

### Training, validation and test sets

![](./img/training_validation_test_sets.png)



<br/>

### Online learning

- data의 양이 너무 많은 경우, 한번에 train 하기 어려우므로 몇개씩 나눠서 모델을 학습
- 이전 데이터로 학습한 모델이 다음 데이터로 계속 학습함



<br/>

### Accuracy

정확도



<br/><br/><br/>

