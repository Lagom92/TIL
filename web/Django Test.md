# Django Test

<br/>

> Django Tutorial을 진행 하던 중 test 코드 작성하는 부분에 의문이 생겨 별도로 공부를 해보려고 한다.

<br/>



- Django는 Project나 App을 생성 하면 tests.py라는 파일이 자동 생성 된다.



<br/>

###  TDD(Test Driven Development)

- 테스트 주도 개발
- 테스트를 해가면서 개발을 하는 소프트웨어 개발 프로세스



<br/>

### unit test

- 독립적인 컴포넌트의(성능이 아닌) 기능적인 동작을 검증한다. 흔히 class나 function 레벨로 수행한다.





<br/>

### 실행 명령어

```
python manage.py test [app name]
```





<br/>

## TestCase

- django.test.TestCase는 unittest의 subclass이다.



<br/>

### class 

- 일반적으로 TestCase를 상속 받는 클래스일 경우 class명의 마지막에 TestCase를 붙인다.(필수 x)

- ex) class SimpleTestCase(TestCase)



<br/>

### Function

- 함수명의 경우 반드시  `test_` 로 시작한다.











<br/>

## Client

- test client는 dummy Web browser처럼 행동하는 python class이다.



<br/>

- 기능
  - URL에 GET, POST request를 simulate하고 response를 확인 할 수 있다.
  - redirect chain을 볼 수 있으며 각 단계에서 URL과 status code를 체크 할 수 있다.



<br/>

```
from django.test import Client
```



<br/>

- page 호출 예시

- 전체 도메인이 아니라 URL의 path만 적는다.

  ```
  Client().get('/login')
  ```

  

<br/>

### timezone.now()

- 현재 시점을 나타내는 날짜시간을 반환한다.
- settings.py에 있는 USE_TZ의 값에 따라 다르다.



- ex)

  ```
  from django.utils import timezone
  
  now_utc = timezone.now()
  print(now_utc)
  # 2020-03-18 04:18:15.979085+00:00
  ```

  





<br/>

### datetime.timedelta()

- 

- ex)

  ```
  import dtetime
  
  day = datetime.timedelta(days=30)
  pirnt(day)
  # 30 days, 0:00:00
  ```





<br/>

- 30일 이후 날짜 출력하기

```
from django.utils import timezone
import datetime

future = timezone.now() + datetime.timedelta(days=30)
print(future)
# 2020-04-17 04:18:15.979085+00:00
```









<br/>

### assertIs()



```
self.assertIs(테스트 조건, 기대값)
```

기대값: boolean







<br/>

<br/>

-------------

### 참고



 https://velog.io/@devzunky/TIL-no.84-Python-Django-Unit-Test 



[timezone.now()_doc](https://docs.djangoproject.com/ko/1.11/ref/utils/#django.utils.timezone.now)







