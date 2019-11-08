# 반응형 웹 페이지 제작

### detect-browser

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



- 추가사항

지금 사용한 npm은 먼가 별로 안이쁨..

나중에 다른걸로 바꾸고 싶다.







----

- 참고

https://www.npmjs.com/package/detect-browser