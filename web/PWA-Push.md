# PWA

Progressive Web App

= 웹 + 앱





# PWA - Push Notification

Firebae Cloud Messaging(FCM)을 이용했다.



- Firebase 프로젝트를 만들기



- Firebase 구성 객체 가져오기

```javascript
var firebaseConfig = {
  apiKey: "api-key",
  authDomain: "project-id.firebaseapp.com",
  databaseURL: "https://project-id.firebaseio.com",
  projectId: "project-id",
  storageBucket: "project-id.appspot.com",
  messagingSenderId: "sender-id",
};
```



- FCM 키 쌍 생성하기 

Firebase 홈페이지 -> 해당 Firebase 프로젝트 -> settings -> 프로젝트 설정 -> 클라우드 메시징 -> 웹 푸시 인증서 -> Generate key pair



- Manifest에 gcm_sender_id 추가

```json
// ./public/manitest.json
{
  ...,
  "gcm_sender_id": "103953800507"
}
```

! '브라우저 발신자 ID'는 Firebase 프로젝트 설정에 표시되는 프로젝트별 발신자 ID와는 다르다.

! manifest.json의 브라우저 발신자 ID는 FCM 자바스크립트 클라이언트에 공통되는 고정된 값이다.



- index.html

```html
// index.html

<script>
// 메시징 객체 검색
const messaging = firebase.messaging();
    
// 앱에서 웹 사용자 인증 정보 구성
messaging.usePublicVapidKey(애클리케이션 ID 키 쌍);

// 알림 수신 권한 요청
Notification.requestPermission().then((permission) => {
  if (permission === 'granted') {
    console.log('Notification permission granted.');
  } else {
    console.log('Unable to get permission to notify.');
  }
});
</script>
```

나의 경우에는 index.html에 넣지 않고 따로 js파일에 넣어줬다.



- 토큰값 가져오기

```javascript
// index.html

messaging.getToken().then(token =>{
    console.log(token)
})
```

`messaging.requestPermission()` 함수가 정상 실행 될 경우(then 일때) `getToken()`을 이용하여 토큰 값을 가져온다.



나중에 이 토큰값을 이곳 저곳에서 사용하기 위해서 Vuex를 이용했다.

```javascript
// store.js

import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    ...
    tokenkey: ""
  }
});

```



```javascript
// index.html
store.state.tokenKey = token;
```

`getToken()`으로 가져온 token을 tokenKey에 넣어줬다.





- firebase-messaging-sw.js 파일 생성(이유나 용도는 아직 모르겠다.)

```javascript
// firebase-messaging-sw.js

importScripts('https://www.gstatic.com/firebasejs/5.5.6/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/5.5.6/firebase-messaging.js');

firebase.initializeApp({
  'messagingSenderId': 프로젝트_messagingSenderId 
});


const messaging = firebase.messaging();

```



- post man을 이용해 알림 보내기(POST 방식)

Headers

| KEY           | VALUE            |
| ------------- | ---------------- |
| Authorization | key={Server Key} |
| Content-Type  | application/json |



Body

```
{
  "notification": {
    "title": "FCM Messagess",
    "body": "This is an FCM Message",
    "icon": "./img/icons/android-chrome-192x192.png"
  },
  "to": console에 나온 token,
  
}
```





- 위 내용을 코드로 변경하면 아래와 같다.

```javascript
const serverKey =
  "key=서버키;
  
 const homeUrl = 프로젝트 URL

export default {
  newPostPush(url) {
    const message = {
      notification: {
        body: "새 포트폴리오가 등록되었습니다.",
        title: "New Portfolio",
        icon: "favicon.ico",
        click_action: homeUrl
      },
      to: "/topics/portfolio"
    };
    fetch(url, {
      method: "POST",
      body: JSON.stringify(message),
      headers: new Headers({
        "Content-Type": "application/json",
        Authorization: serverKey
      })
    })
      .then(response => {
        if (response.status < 200 || response.status >= 400) {
          throw "Error subscribing to topic: " + response.status + " - " + response.text();
        }
      })
      .catch(error => {
        console.log("error: ",error)
      });
  },

```









---

**Reference**

[FCM을 활용한 웹 푸시 구현_Blog](https://dongsik93.github.io/til/2019/07/31/til-etc-fcm/)

[자바스크립트 프로젝트에 Firebase 추가](https://firebase.google.com/docs/web/setup)

[자바스크립트 FCM 클라이언트 앱 설정](https://firebase.google.com/docs/cloud-messaging/js/client)

[Instance ID](https://developers.google.com/instance-id/reference/server?hl=ko#create_relationship_maps_for_app_instances)