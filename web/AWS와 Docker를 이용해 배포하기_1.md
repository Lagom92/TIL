# Docker



![](./img/docker-logo.png)



## What ?

도커 란 ?

리눅스의 응용 프로그램들을 소프트웨어 컨테이너 안에 배치시키는 일을 자동화하는 오픈 소스 프로젝트이다.





#### 이미지

필요한 프로그램과 라이브러리, 소스들을 설치 한 뒤 파일로 만든 것

이 이미지를 저장소에 올리고 받을 수 있다.



#### 컨테이너

이미지를 실행한 상태

이미지로 여러개의 컨테이너를 만들 수 있다.







## Why ?

도커를 사용하는 이유 ?





리눅스 운영체제에서 docker를 사용하는 경우 sudo 권한 으로 인해 sudo docker... 라고 항상 명령어를 입력해야 한다.

이는 너무 번거러우므로 docker를 항상 sudo 권한으로 실행 하도록 한다.

```
# 현재 접속 중인 사용자에게 권한 주기
sudo usermod -aG docker $USER

# or

# 지정한 유저에 권한 주기
sudo usermod -aG docker <유저명>
```

나갔다가 다시 들어와야 적용이 된다.



확인을 하고 싶다면

```
docker run hello-world
```

를 입력해 보자.





## 명령어



#### 도커 이미지 가져오기

```
$ docker pull [이미지 이름]:[태그]

# ex)
# docker pull centos:7
```



#### 이미지 확인하기

```
$ docker images
```



#### 컨테이너 생성하기

```
$ docker create [옵션] [이미지 이름]:[태그]

# ex)
# docker create -i -t centos:7
```

- -i : 상호 입출력
- -t : TTY를 활성화 하여 bash 쉘을 사용





#### OPTION Description

| -i     | Interative<br />STDIN(키보드 입력)을 컨테이너로전달할 수 있는지에 대한 여부 |
| ------ | ------------------------------------------------------------ |
| -t     | psuedo TTY<br />가상 터미널 모드<br />컨테이너 내에 터미널로 접속하려면 필요 |
| -d     | Daemon으로 실행 시킬 것인지에 관한 여부<br />이 옵션을 주면 백그라운드로 실행이 가능하다. |
| --rm   | 컨테이너의 프로세스 종료 시 컨테이너가 자동으로 삭제될 것인지에 대한 여부 |
| --name | 컨테이너의 이름                                              |
| -p     | 포트 포워딩<br />[호스트의 포트]:[컨테이너 내의 포트]로 옵션 값 지정 |
| -e     | 환경 변수<br />[변수명] = [값]으로 옵션 값 지정              |
| -v     | 볼륨 설정<br />[호스트의 디렉토리]:[컨테이너 내의 디렉토리]로 옵션 값 지정 |





## Dockerfile

웹 어플리케이션을 살행하기 위해 서버에서 준비해야 할 모든 작업을 나열한 파일

Docker의 자체 언어를 사용하여 이미지를 생성하는 과정을 작성한 파일



```
FROM python:3.7 # 기본 이미지를 python3.7 로 설정
ENV PYTHONUNBUFFERED 1 # 환경변수 설정 삭제할까?
RUN mkdir /code # docker 내에서 /code 라는 이름의 폴더 생성
WORKDIR /code # docker 내에서 코드를 실행할 폴더 위치를 /code 로 지정
ADD requirements.txt /code/ # 로컬의 requirements.txt 파일을 docker /code/ 폴더로 마운트
RUN pip install -r requirements.txt # docker 내 requirements.txt 파일을 이용하여 패키지 설치
ADD . /code/ # 로컬 내 현재 위치에 있는 모든 파일 및 폴더를 docker 의 /code/ 폴더로 마운트
```



```
FROM python:3.7.7	# 기본 이미지를 python 3.7.3으로 설정

RUN mkdir /code	# docker 내에서 /code 라는 이름의 폴더 생성
WORKDIR /code	# docker 내에서 코드를 실행 할 폴더 위치를 /code로 지정
COPY django ./

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "sample.wsgi", "--bind=0:8000"]
```





### ps

모든 컨테이너 목록을 출력

```
docker ps 
```

정지된 컨테이너까지 모두 출력

```
docker ps -a
```









- docker 제거

```
docker rm <컨테이너>
```



```
docker rmi <이미지 id>
```





- 도커 빌드

```
docker build -t <이름> .
```

이름: nginx.conf의 serve 포트 앞 이름



- 실행

```
docker run -it -p 8000:8000 <>
```



- background에서 도커가 돌아가게 하기

```
docker run -d -p 8000:8000 <이미지 이름>
```



- background 중지

```
docker stop <컨테이너 id>

or

docker attach <컨테이너 id>
```



-ing





### Django Create super

- 관리자 계정이 필요한데 명령어를 입력해서 넣어줬다.
- CONTAINER ID: django 일때

```
docker exec -it django python manage.py shell -c "from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.create_superuser('admin', 'admin@gmail.com', 'password')"
```

아이디는 admin

이메일은 admin@gmail.com

비밀번호는 password





------------------------

### 참고

[공식 사이트](https://www.docker.com/)

[왜 굳이 도커를 써야 하나요?](https://www.44bits.io/ko/post/why-should-i-use-docker-container)



https://nachwon.github.io/django-deploy-8-docker/



http://it.plusblog.co.kr/220979998005



https://www.slideshare.net/raccoonyy/django-164557454