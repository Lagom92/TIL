# jupyter 백그라운드에서 사용하기



<br/>

### 사용법

<br/>

- 기본

```
nohup [프로세스] &
```

or

```
nohup jupyter notebook --ip 아이피주소 &
```





<br/>

- nohup.out 파일을 생성하지 않는 경우

```
nohup [프로세스] 1>/dev/null 2>&1 &
```



<br/>

- jupyter notebook 토큰 확인

```
jupyter notebook list
```



<br/>

- 작업 번호(PID) 확인하기

```
jobs
```

or

```
ps -l | grep jupyter
```

or

```
ps -e
```





<br/>

- notebook 끄기

```
kill -9 [작업 번호]
```





### 명령어 의미

- nohup: 터미널과 독립적으로 프로세스를 실행, 터미널이 끊겨도 프로세스는 계속 동작
- &: 프로세스를 백그라운드에서 실행
- 1>/dev/null: 표준 출력을 사용하지 않겠다는 의미
- 2>&1: 표준 에러를 표준 출력과 같게 만드는 명령어 



<br/>

<br/>

--------------

<br/>

### Reference

- https://gracefulprograming.tistory.com/128

- https://datarami.tistory.com/7

