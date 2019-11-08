# Getting started with Google Kubernetes Engine



## Containers and Docker v1.6

- 컨테이너를 사용하면 프로그램이나 프로세스를 서로 분리 할 수 있다.
- 프로그램에 문제를 일으키지 않으면서도 배포를 간편하게 만들 수 있다.
- 기반 기술에 친숙하지 않은 사용자도 쉽게 사용할 수 있다.



## 실습

## Docker 이미지로 빌드, 실행, 배포하는 방법



### 설정

> 실습을 시작하기 전 아이디와 비밀번호를 제공해 준다. 이 아이디를 이용해 접속을 해야 미리 만들어진 VM 인스턴스를 이용할 수 있다. 만약 자신의 아이디를 사용한다면 VM인스턴스에 아무것도 없는것을 보게 될 것이다.



- 탐색 메뉴 아이콘 -> 컴퓨팅 -> Compute Engine -> VM 인스턴스

![](C:\Users\multicampus\Desktop\img\cloud\vm.PNG)



- `k8s-workshop-module-1-lab`라는 이름의 인스턴스가 있는것을 확인할 수 있다.

![](C:\Users\multicampus\Desktop\img\cloud\vm2.PNG)



- SSH 드롭다운 -> 브라우저 창에서 열기를 선택한다.

![](C:\Users\multicampus\Desktop\img\cloud\ssh.PNG)



- 아래와 같은 창이 나오는것을 확인 한다.

![](C:\Users\multicampus\Desktop\img\cloud\ssh2.PNG)



- 인스턴스가 완전히 프로비저닝 되어있는지 확인한다.

```
ls /
```

![](C:\Users\multicampus\Desktop\img\cloud\ls.PNG)

디렉토리가 없으면 몇 분을 기다려 본다.





### Docker로 컨테이너 실행 및 배포

Docker를 사용하면 반복 가능한 실행 환경에서 애플리케이션을 컨테이너로 간편하게 패키징 할 수있다.

Python으로 작성된 웹 서버가 포함된 Docker 컨테이너 이미지를 생성 및 실행

Docker 탐색

Docker 레지스트리에 업로드 및 공유

아래의 실습을 통해 알게 될것

- Docker 이미지 빌드하기
- Docker 이미지를 Google Cloud 레지스트리에 푸시
- Docker 컨테이너 실행



### 웹 서버를 수동으로 실행



- `/kickstart` 폴더로 이동

```
cd /kickstart
```

![](C:\Users\multicampus\Desktop\img\cloud\cd.PNG)



- 콘텐츠 목록 표시

```
ls -1h
```

![](C:\Users\multicampus\Desktop\img\cloud\ls -1h.PNG)

`Dockerfile` 및 `web-server.py`가 있는지 확인한다.

`web-server.py`는 localhost:8888에서 HTTP 요청에 응답하고 호스트 이름을 출력하는 웹 서버를 실행하는 Python 애플리케이션이다.



- python 및 PIP의 최신 버전을 설치 한다.

```
sudo apt-get install -y python3 python3-pip
```

![](C:\Users\multicampus\Desktop\img\cloud\install-py.PNG)



- Tornado 라이브러리를 설치 한다.

```
pip3 install tornado
```

![](C:\Users\multicampus\Desktop\img\cloud\pip-toran.PNG)



- 백그라운드에서 Python 애플리케이션을 실행한다.

```
python3 web-server.py &
```

![](C:\Users\multicampus\Desktop\img\cloud\server.PNG)



- 웹 서버에 액세스 할 수 있는지 확인한다.

```
curl http://localhost:8888
```

![](C:\Users\multicampus\Desktop\img\cloud\host.PNG)

`Hostname: k8s-workshop-module-1-lab` 가 나와야 한다.



- 웹 서버를 종료한다.

```
kill %1
```

![](C:\Users\multicampus\Desktop\img\cloud\terminate.PNG)





### Docker를 사용하여 패키징

Docker 이미지는 Dockerfile로 설정되며 Docker는 이미지를 스태킹할 수 있게 해준다.

Docker 이미지는 Python이 사전 설치되어 있는 기존 Docker 이미지 라이브러리/Python을 기반으로 생성된다.



- Dockerfile을 확인한다.

```
cat Dockerfile
```

![](C:\Users\multicampus\Desktop\img\cloud\cat.PNG)



- 웹 서버가 포함된 Docker 이미지를 빌드한다.
- 이미지는 로컬 이미지 스토어에 저장된다.

```
sudo docker build -t py-web-server:v1 .
```

![](C:\Users\multicampus\Desktop\img\cloud\web-server.PNG)

명령어 끝에 `.` 를 포함해야 한다. 이렇게 해야 현재 작업 디렉토리에 이미지를 저장하라고 Docker에 지시를 내린다.



- Docker를 사용하여 웹 서버를 실행한다.

```
sudo docker run -d -p 8888:8888 --name py-web-server -h my-web-server py-web-server:v1
```

![](C:\Users\multicampus\Desktop\img\cloud\웹 서버 실행.PNG)



- 웹 서버에 다시 엑세스 해본 다음 컨테이너를 중단한다.

```
curl http://localhost:8888
```

```
sudo docker rm -f py-web-server
```

![](C:\Users\multicampus\Desktop\img\cloud\localhost2.PNG)

![](C:\Users\multicampus\Desktop\img\cloud\컨테이너 중지.PNG)

`python` 및 `tornado` 라이브러리를 비롯한 모든 종속 항목과 웹 서버가 하나의 Docker 이미지로 패키징되어 모두와 공유할 수 있다.

 `py-web-server:v1` Docker 이미지는 모든 Docker 지원 OS(OS X, Windows, Linux)에서 동일한 방식으로 작동한다.



### 이미지를 레지스트리에 업로드

Docker 이미지는 Docker 레지스트리에 업로드해야 다른 머신에서 사용할 수 있다.

Docker 이미지를 Google Cloud 레지스트리(gcr.io)의 비공개 이미지 저장소에 업로드한다.



- `sudo` 없이 Docker 명령어를 실행할 수 있도록, Docker 그룹에 로그인된 사용자를 추가하고 Container Registry 사용자 인증 정보 도우미를 사용하여 이미지를 인증된 사용자로서 저장소에 푸시한다.

```
sudo usermod -aG docker $USER
```

![](C:\Users\multicampus\Desktop\img\cloud\유저.PNG)



- 그룹 변경사항이 적용되도록 `SSH` 세션을 다시 시작하고 `kickstart` 디렉터리로 돌아온다.

```
cd /kickstart
```

![](C:\Users\multicampus\Desktop\img\cloud\다시 cd.PNG)



- GCP 프로젝트 이름을 환경 변수에 저장한다.

```
export GCP_PROJECT=`gcloud config list core/project --format='value(core.project)'`
```

![](C:\Users\multicampus\Desktop\img\cloud\환경변수.PNG)



- `gcr.io`를 호스트 이름으로, 프로젝트 ID를 프리픽스로 포함하는 레지스트리 이름으로 Docker 이미지를 다시 빌드한다.

```
docker build -t "gcr.io/${GCP_PROJECT}/py-web-server:v1" .
```

![](C:\Users\multicampus\Desktop\img\cloud\gcr.io.PNG)



### 공개적으로 액세스할 수 있도록 이미지 설정

Google Container Registry는 Google Cloud Storage에 이미지를 저장한다.



- gcloud를 Container Registry 사용자 인증 정보 도우미로 사용하도록 Docker를 구성한다.(이 작업은 한 번만 수행하면 됨)

```
PATH=/usr/lib/google-cloud-sdk/bin:$PATH
gcloud auth configure-docker
```

메시지가 표시되면 **ENTER** !

![](C:\Users\multicampus\Desktop\img\cloud\gcloud.PNG)



- 이미지를 `gcr.io`에 푸시한다.

```
docker push gcr.io/${GCP_PROJECT}/py-web-server:v1
```

![](C:\Users\multicampus\Desktop\img\cloud\이미지 푸시.PNG)



- Google Cloud Storage 저장소에 버킷(객체)으로 저장된 이미지를 보려면 **탐색 메뉴** 아이콘을 클릭하고 **스토리지**를 선택한다.

![](C:\Users\multicampus\Desktop\img\cloud\이미지 확인.PNG)



- 공개적으로 액세스할 수 있도록 이미지 저장소를 설정하려면 Google Cloud Storage에서 권한을 업데이트한다.

```
gsutil defacl ch -u AllUsers:R gs://artifacts.${GCP_PROJECT}.appspot.com
gsutil acl ch -r -u AllUsers:R gs://artifacts.${GCP_PROJECT}.appspot.com
gsutil acl ch -u AllUsers:R gs://artifacts.${GCP_PROJECT}.appspot.com
```

![](C:\Users\multicampus\Desktop\img\cloud\권한 업데이트1.PNG)

![](C:\Users\multicampus\Desktop\img\cloud\권한 업데이트2.PNG)

![](C:\Users\multicampus\Desktop\img\cloud\권한 업데이트3.PNG)

그러면 GCP 프로젝트에 대한 액세스 권한을 보유한 모두가 이미지를 사용할 수 있게 된다.



### 원하는 머신에서 웹 서버 실행



- 다음 명령어를 실행하여 Docker를 설치한 모든 머신에서 Docker 이미지를 실행할 수 있다.

```
docker run -d -p 8888:8888 -h my-web-server gcr.io/${GCP_PROJECT}/py-web-server:v1
```

![](C:\Users\multicampus\Desktop\img\cloud\웹 서버 실행 2.PNG)

VM 인스턴스에서 이를 테스트할 수 있다.(위의 `curl` 명령어를 다시 사용)



- 실습 환경을 종료하고 Cloud Shell로 돌아간다.

```
exit
```

![](C:\Users\multicampus\Desktop\img\cloud\exit 끝.PNG)



----------------------------------------------------------------------------------------------------



##### 출처

[Getting started with Google Kubernetes Engine](https://www.coursera.org/learn/google-kubernetes-engine)