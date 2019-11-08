

# reshape ?



- 행렬 계산을 위하여 Y데이터의 사이즈를 (len(Y),1)로 저장합니다.

```
Y = Y.reshape(-1, 1)
```



기존 데이터는 유지하고 차원과 형상을 바꾼다.



파라미터로 입력한 차원에 맞게 변경한다.

-1 로 설정하면 나머지를 자동으로 맞춘다.



! 바꾸는 개수가 나누어 지지 않는다면 

! ValueError: cannot reshape array of size 에러가 발생





http://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221415471793&parentCategoryNo=&categoryNo=50&viewDate=&isShowPopularPosts=true&from=search





# 행렬 곱 연산

matmul

dot

@



http://blog.naver.com/PostView.nhn?blogId=cjh226&logNo=221356199190&categoryNo=17&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView







!

'list' object has no attribute 'reshape'



!

Cannot cast ufunc subtract output from dtype('float64') to dtype('int32') with casting rule 'same_kind'







------------------------



# 행렬

아~~

어렵다~



- numpy 사용하는 이유

파이썬은 자체적으로 배열 자료형을 제공하지 않는다.

그래서 Numpy를 사용한다.



Numpy의 배열 연산은 C로 구현된 내부 



- Numpy 패키지 임포트

```
import numpy as np
```



- Numpy의 array라는 함수에 리스트를 넣으면 배열로 변환해 준다.



- 1차원 배열 만드는법

```
list = [1, 2, 3, 4]
ar = np.array(list)
ar

# array([1, 2, 3, 4])
```

```
type(arr)

# numpy.ndarray
```



- 2차원 배열 만드는법

```
c = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array
c
```

```
array([[0, 1, 2],
       [3, 4, 5]])
```



```
# 행의 갯수
len(c)

# 열의 갯수
len(c[0])
```



### axis 파라미너



- 다차원 배열의 축(axis)

그림 추가

http://taewan.kim/post/numpy_sum_axis/



default = None



- axis = None



- axis = 1 



- axis = 2



- axis = 3







http://taewan.kim/post/numpy_cheat_sheet/





matmul 과 dot의 차이점

http://blog.naver.com/PostView.nhn?blogId=cjh226&logNo=221356199190&categoryNo=17&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView



http://blog.naver.com/PostView.nhn?blogId=cjh226&logNo=221356884894&parentCategoryNo=&categoryNo=17&viewDate=&isShowPopularPosts=false&from=postView

1. dot는 행렬과 상수의 곱셈을 허용, matmul은 error발생
2. 3차원 이사의 행렬곱을 실행할때 결과가 다름















--------------------

csv 파일 읽기!



```
import pandas as pd

data = pd.read_csv("advertising.csv", skiprows=[0,0], header=None)
X = data.values[:, 1:4]
Y = data.values[:, 4]
```





블로그에 올렸음

---------------------------------







# 학습률

자동으로 변경을 해주는 방법을 찾아보자

아담이나

경사하강법 이나 등등



