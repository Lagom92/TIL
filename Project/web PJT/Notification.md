# 반응형 웹 페이지 제작

### Notification



##### 방법 1

###### detect-browser

현재 접속한 브라우저가 무엇인지 확인하고 원하는 브라우저가 아닐경우 경고창을 띄우거나 할 수 있다.



- install

```
npm i detect-browser
```



- main.js

```
const { detect } = require('detect-browser');
const browser = detect();

// handle the case where we don't detect the browser
switch (browser && browser.name) {
  case 'chrome':
    console.log('supported');
    break;

  default:
    console.log('not supported');
		alert('해당 사이트는 크롬에 최적화 되어 있습니다.')
}
```





##### 방법 2

이 방법이 더 좋아보인다.



- NotificationAlert.vue

```
<script>
var isChrome = !!window.chrome && (!!window.chrome.webstore || !!window.chrome.runtime);
window.onload = function () {
            if (window.Notification) {
                Notification.requestPermission();
                notify();
            }
        }
        function notify() {
            if (Notification.permission !== 'granted') {
                alert('알림을 허용해주세요!');
            }
            else {
                if (!isChrome){
                    var notification = new Notification('해당 사이트는 크롬에 최적화 되어 있습니다.', {
                        icon: "./img/chrome.png"
                    });
                }
            }
        }
</script>

```



- HomePage.vue

```
import NotificationAlert from '../components/NotificationAlert'
```

```
export default {
name: 'HomePage',
components: {
	....
	NotificationAlert,
}
}
```





----

참고

https://developer.mozilla.org/ko/docs/Web/API/notification

