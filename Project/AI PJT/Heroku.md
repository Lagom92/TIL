# Heroku



```
npm install -g heroku
```









와~~~~~~~~~~~~~~~~~~~~

- app.py

```
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
```



```
app.run(host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT',8080)))
```



- Prodfile

```
web: python app.py
```

웹을 키면 app.py를 실행한다



- requirements.txt

```

```

freeze > requirements.txt

설치된 라이블러리들이 txt에 들어감



- runtime.txt

```
python-3.7.3
```







Heroku CLI 명령어들

```
heroku login
```



```
heroku create <저장소 이름>
```

git 저장소가 생성된 폴더에서 사용 가능한 명령어

heroku에 저장소를 생성하고 현재 git 저장소에 heroku 저장소 위치를 <저장소 이름> 라는 이름으로 기억시킨다.

이 이름은 모든 heroku 사용자간에 중복이 없어야 한다.





Heroku 저장소로 코드 올리기

heroku create로 heroku 저장소가 생성되면 현재 폴더의 git에 heroku 저장소 주소가 <저장소 이름>으로 기억된다

heroku 저장소에 push하면 사이트가 자동으로 인터넷에 등록된다.

```
git push heroku master
```

heroku 저장소에 master branch를 push 하는 명령어



! master 브랜치에서 해야한다.







- 환경변수 넣어주는 방법 1 - heroku 사이트에서 실행

Dashboard > settings > Config Vars 눌러서 Add !!