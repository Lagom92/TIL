# Firebase deploy

### firebase를 이용해서 deploy 하기



1. node.js 및 npm 설치



2. Firebase CLI 설치

```cmd
$ npm install -g firebase-tools
```



3. Google 계정으로 Firebase 로그인

```cmd
$ firebase login
```



- 만약 로그아웃을 하여 계정을 변경하고 싶은 경우

  ```cmd
  $ firebase logout
  ```

  

4. 모든 Firebase 프로젝트를 나열

```cmd
$ firebase list
```



5. 최신 버전으로 CLI 업데이트

```cmd
$ npm install -g firebase-tools
```



6. Firebase 프로젝트 초기화

```cmd
$ firebase init
```



7. json파일 변경

```json
// firebase.json
{
    "hosting": {
        "public": "dist"
    }
}
```



```json
// firebase.json
{
  "hosting": {
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```



8. dist폴더 생성

```cmd
$ npm run build
```



9. 배포

```cmd
$ firebase deploy
```





### 배포 후 업데이트 할때

1. 

```
$ npm run build
```

or

```
yarn build
```



2. 

```
firebase deploy
```





참고



[Vue CLI](https://cli.vuejs.org/guide/deployment.html#firebase)

[파이어베이스 배포 관련 블로그](https://codingmania.tistory.com/298)

[Firebase Functions_유튜브](https://www.youtube.com/watch?v=DYfP-UIKxH0&list=PLl-K7zZEsYLkPZHe41m4jfAxUi0JjLgSM)