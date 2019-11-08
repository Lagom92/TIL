## CSV

Comma Separated Values

몇 가지 필드들을 쉼표(`,`)로 구분한 텍스트 데이터 및 텍스트 파일



확장자: `.csv`

비슷한 포맷으로는 TSV(탭으로 구분) 나 SSV(반각 스페이스로 구분)가 있다.

엑셀 양식의 데이터를 프로그램에 상관없이 쓰기 위한 데이터 형식



- 아래는 csv 파일을 읽는 코드의 예시이다.

```
import csv

f = open('advertising.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
   print(line)
f.close()
```



- 파일을 계속 열고 있을 필요가 없으므로 `with as` 문을 이용해서 파일을 닫는 과정을 생략하기도 한다.

```
with open('advertising.csv') as csvfile:
   rdr = csv.reader(csvfile)
   for i in rdr:
      print(i)
```



> csv 파일의 첫번째 줄에 header로서 당장 필요없는 데이터가 있다.
>
> 어떻게 없애지?.... next함수를 찾았다.



- next() 함수

```
# skip the headers
next(rdr, None)
```



- 문자열로 값이 넣어져버렸다.. 그래서 float를 사용해서 숫자로 바꿔줬다.

```
for i in rdr:
    X.append([float(i[1]), float(i[2]), float(i[3] )]) 
    Y.append([float(i[4])])
```





참고

[위키백과](https://ko.wikipedia.org/wiki/CSV_(%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D))

[csv파일 읽기와 쓰기](https://python.flowdas.com/library/csv.html)



----------------------------------------------



## sklearn의 train_test_split() 사용법



다양한 기계학습과 데이터 분석 툴을 제공하는 scikit-learn 패키지 중 model_selection에는 데이터 분할을 위한 train_test_split 함수가 있다.



train_test_split 함수는 전체 데이터셋 배열을 받아서 랜덤하게 test/train 데이터 셋으로 분리해주는 함수이다.



- 클래스 값을 포함하여 하나의 데이터로 받는 경우

```
df_train, df_test = train_test_split(df, test_size=0.4, random_state=0)
```



- 클래스를 개별의 배열로 받는 경우

```
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.5)
```





```
from sklearn.model_selection import train_test_split


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=321)
```



#### Parameter

**arrays** : 분할시킬 데이터를 입력 *(Python list, Numpy array, Pandas dataframe 등..)*

**test_size** : 테스트 데이터셋의 비율(float)이나 갯수(int) *(default = 0.25)*

**train_size** : 학습 데이터셋의 비율(float)이나 갯수(int) *(default = None)*, None을 입력하고 test_size를 지정할 경우 테스트 데이터셋을 뺀 나머지를 훈련 데이터로 사용한다. 

**random_state** : 데이터 분할시 셔플이 이루어지는데 이를 위한 시드값 *(int나 RandomState로 입력)*

**shuffle** : 셔플여부설정 *(default = True)*





참고

[train_test_split() 사용법_Blog](http://blog.naver.com/PostView.nhn?blogId=siniphia&logNo=221396370872&parentCategoryNo=&categoryNo=22&viewDate=&isShowPopularPosts=true&from=search)

[로보리포트_기계학습 훈련 데이터 구성 방법](https://roboreport.co.kr/%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5-%ED%9B%88%EB%A0%A8-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B5%AC%EC%84%B1-%EB%B0%A9%EB%B2%95/)





-----------------------------------



## LinearRegression() 함수



scikit-learn 패키지를 사용하여 선형 회귀분석을 하는 경우 linear_model 서브 패키지의 LinearRegression 클래스를 사용한다.



- LinearRegression 클래스 객체 생성

```
lrmodel = LinearRegression()
lrmodel.fit(X_train, Y_train)
```



`fit` 메서드로 모형 추정. 상수항 결합을 자동으로 해주므로 사용자가 직접 `add_constant` 등의 명령를 써서 상수항 결합을 할 필요는 없다.



- coef

추정된 가중치 벡터

가중치들을 보여준다.

```
lrmodel.coef_
```



- intercept

추정된 상수항

절편을 나타낸다.

```
lrmodel.intercept_
```



- `_`  는 머신러닝에서 유도된 결과를 나타내는 기호이다.







참고

[데이터 사이언스 스쿨_선형 회귀분석의 기초](https://datascienceschool.net/view-notebook/58269d7f52bd49879965cdc4721da42d/)

[scikit-learn_LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)



------------------------



## Mean squared error



MSE(평균 제곱 오차, Mean squared error)



손실함수는 정답에 대한 오류를 숫자로 나타내는 것으로 오답에 가까울수록 큰 값이 나온다. 반대로 정답에 가까울수록 작은 값이 나온다.



알기 쉽고 계산하기도 쉬워서 추청한 값에 대한 정확도 측정을 위해 주로 사용된다.



```
from sklearn.metrics import mean_squared_error

y_true = [[0.5, 1],[-1, 1],[7, -6]]
y_pred = [[0, 2],[-1, 2],[8, -5]]
mean_squared_error(y_true, y_pred)
```





참고

[딥러닝 손실함수_Blog](https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221025759001&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

[scikit-learn_mean_squared_error()](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)



---------------



## pickle 모듈

데이터를 저장하고 불러올때 매우 유용한 라이브러리

클래스 자체를 파일로 저장했다가 그것을 그대로 불러올 수 있다.

원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드할 수 있다.

데이터를 저장하거나 불러올때 바이트 형식으로 읽거나 쓴다(wb, rb).

binary형태로 저장되기 때문에 용량이 작아진다.



```
import pickle
```



```
# save
data = ['a', 'b', 'c']
with open('data.txt', 'wb') as f:
    pickle.dump(data, f)
```



```
# load
with open('data.txt', 'rb') as f:
    data = pickle.load(f)
```



참고

[pickle 모듈_Blog](https://wayhome25.github.io/cs/2017/04/04/cs-04/)

[python snippets_pickle](https://wikidocs.net/8929)

[파이썬 객체 직렬화](https://docs.python.org/ko/3/library/pickle.html)

