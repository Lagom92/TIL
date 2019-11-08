# Logistic regression



- 이메일이 스팸인지 아닌지, 종양이 양성인지 음성인지 등 어떤 기준을 가지고 어떤것을 분류하는 문제를 Classification problem 이라고 한다.



- 분류문제의 경우 선형회귀가 잘 표현하지 못 하는 경우가 발생 할 수 있다.



- sigmoid function 혹은 logistic function

함수 ; 
$$
g(z) = 1 / 1+ e^-z
$$






- Simplified Cost Function

```
Cost(hθ(x),y)=−ylog(hθ(x))−(1−y)log(1−hθ(x))
```





```
J(θ)=−1m∑i=1m[y(i)loghθ(x)+(1−y(i))log(1−hθ(x))]
```











-----------------

Reference



http://gnujoow.github.io/ml/2016/01/29/ML3-Logistic-Regression/



https://github.com/SSaishruthi/LogisticRegression_Vectorized_Implementation/blob/master/Logistic_Regression.ipynb





https://github.com/proauto/ML_Practice/blob/master/LogisticRegression.py



https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148



https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc



https://github.com/SSaishruthi/LogisticRegression_Vectorized_Implementation/blob/master/Logistic_Regression.ipynb



https://wikidocs.net/4289