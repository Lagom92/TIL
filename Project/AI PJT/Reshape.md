# Reshape



- 행렬 계산을 위하여 Y데이터의 사이즈를 (len(Y),1)로 저장합니다.

```
Y = Y.reshape(-1, 1)
```



기존 데이터는 유지하고 차원과 형상을 바꾸는데 사용한다.

파이썬 Numpy에서 배열의 차원을 재구조화, 변경하고자 할 때 reshape() a메소드를 사용한다.



파라미터로 입력한 차원에 맞게 변경한다.

-1 로 설정하면 나머지를 자동으로 맞춘다.



```
.reshape(행, 열)
```





예를 들어 3행 4열로 구성된 2차원의 배열로 재설정 하고자 한다면 reshape(3, 4)을 해주면 된다.



- reshape에서 -1의 의미

변경된 배열의 '-1' 위치의 차원은 "원래 배열의 길이와 남은 차원으로 부터 추정"이 된다는 의미이다.

One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions.

즉, -1로 설정하면 나머지를 자동으로 맞춰준다고 생각해도 무방하다.



! 바꾸는 개수가 나누어 지지 않는다면 

! ValueError: cannot reshape array of size 에러가 발생





order 파라미터 ??

지정된 index 순서에 따라 형상을 변환한다.

C : 

C형식 index 순서

뒤 차원부터 변경하고 앞 쪽 차원을 변경

(default = C)



F : 

포트란 형식 index 순서

앞 차원부터 변경하고 뒤쪽 차원을 변경







참고

http://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221415471793&parentCategoryNo=&categoryNo=50&viewDate=&isShowPopularPosts=true&from=search



https://rfriend.tistory.com/345



