# PWA



- 크롬 카나리아 다운로드
- node.js 다운로드(LTS)



pwa의 특징

Responsive_반응형

App-like

Discoverable

Engageable

Connectibity

Safe





## Manifest.json

앱이 사용자에게 표시되는 방식을 제어하는 기능을 제공



- 예시 코드

```json
// ./public/manifest.json
{
  "name": "vue-pwa-tutorial",
  "short_name": "vue-pwa-tutorial",
  "icons": [
    {
      "src": "./img/icons/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "./img/icons/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "#000000",
  "theme_color": "#4DBA87"
}
```





- Start URL

웹 앱이 시작되는 지점

- Launch Image

웹 앱 시작 화면

- Display Type

웹 앱의 화면 형태

- Display Orientation

웹 앱 화면 방향

- App Icon

앱 아이콘 이미지와 크기



추가 예정 .....



----

----







# Service Worker



- [chrome://serviceworker-internals](chrome://serviceworker-internals/)





특징

- 브라우저의 백그라운드에서 실행되며 웹 페이지와 별개의 라이프 싸이클을 가진다
- 네트워크 요청을 가로챌 수 있어 해당 자원에 대한 캐쉬 제공 또는 서버에 자원을 요청할수 있다
- 브라우저 종속적인 생명주기로 백그라운드 동기화 기능을 제공한다
- Web 과 Mobile Push 수신이 가능하도록 Notification기능을 제공한다.
- navigator.serviceworker 로 접근
- 기존 JS와의 별개의 자체 스코프를 가진다
- DOM에 직접적으로 접근이 불가능하다 - postMessage()를 이용
- 사용하지 않을 때 자체적으로 종료, 필요시에 다시 동작(event-driven 방식)



쓰레드 ?

프록시 ?

DOM ?



shared worker ?







Service Worker 등록

register() 사용

index.html에 작성

sw.js 파일 생성



- 방법1

```
<script> 
if ("serviceWorker" in navigator) {
	// 간단한 실행
	navigator.serviceWorker.register("/sw.js");
}
</script>
```



- 방법2

```
if ("serviceWorker" in navigator) {
	// Promis 사용
	navigator.serviceWorker.register("/sw.js")
	.then(function (reg) {
		// 성공하면
		console.log("worked!", reg);
	}).catch(function (err) {
		// 에러가 발생하면
		console.log("error occured!!", err);
	})
}
```





service worker 설치

등록과 설치 ?

서비스 워커에 관한 파일을 등록하는것

캐싱을 하는것 - 설치



- register() 에서 등록한 스크립트 파일에서 install() 호출

```
self.addEventListener("install", function(event) {
	// 캐쉬 등록 또는 기타 로직 수행
});
```





```
var CACHE_NAME = 'cache-v1';
var filesToCache = [
	'/',
	
]
```

CACHE_NAME: 캐쉬를 담을 파일명 정의

filesToCache: 캐쉬할 웹 자원들 정의



```
self.addEventListener("install", function(event) {
event.waitUntil(
	caches.open(CACHE_NAME).then(function(cache) {
	// 위에 지정한 캐쉬 목록을 'cache-v1' 캐쉬에 추가
	return cache.addAll(filesToCache);
	})
);
});
```



waitUntil() :





self ?

예약어 caches ?

sw toolsbox ?





Service Worker 네트워크 요청 응답

service worker 설치 후 캐쉬된 자원에 대한 네트워크 요청이 있을 때는 캐쉬로 돌려준다

```
self.addEventListener("fetch", function(event) {
	event.respondWith(
		caches.match(event.request).then(function(response) {
		if (response) {
		return response;
		}
		return fetch(event.request);
		})
	);
});
```



respondWith() : Fetch 이벤트의 응답(response)을 반환

match() : 해당 request에 상응하는 캐쉬가 있으면 찾아서 돌려주고 아니면 fetch() 로 자원 획득





Service Worker 활성화 및 업데이트

새로운 서비스워커가 설치되면 활성화 단계로 넘어온다

이전에 사용하던 서비스워커와 이전 캐쉬는 모두 삭제하는 작업 진행



```
self.addEventListener("fetch", function(event) {
  var newCacheList = ["cache-v1"];

  event.waitUntil(
    caches.keys()
    .then(function(cacheList) {
      return Promise.all(
        cacheList.map(function(cacheName) {
        // 새로운 서비스 워커에서 사용할 캐쉬 이외의 캐쉬는 모두 삭제
          if (newCacheList.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      )
    })
    .catch(function(err) {
      return console.log(err)
    })
  );
});
```





map ?

```
var arr = [1, 2, 3]

arr.map(function(e) {
return e + 10;
})

// [11, 12, 13]
```







Service Worker 라이프 싸이클

서비스워커는 웹 페이지와 별개의 생명주기

서비스워커 등록, 설치, 활성화 과정을 보면

- 웹페이지에서 서비스워커 스크립트 호출
- 브라우저 백그라운드에서 서비스워커 설치
- 설치 과정에서 정적 자원 캐싱(Cache 실패시 설치 실패)
- 설치 후 활성화, 네트워크 요청에 대한 가로채기 가능

사용하지 않을 때는 휴지상태, 필요시에만 해당 기능 수행

메모리 상태에 따라 자체적으로 종료하는 영리함







라이브러리

sw-toolbox

sw-precache

```
npm install -global sw-precache
```





workbox







---

- index.html

```
// service worker
      if ("serviceWorker" in navigator) {
      	// Promis 사용
      	navigator.serviceWorker.register("/sw.js")
      	.then(function (reg) {
      		// 성공하면
      		console.log("sw worked!", reg);
      	}).catch(function (err) {
      		// 에러가 발생하면
      		console.log("sw error occured!!", err);
      	})
      }
```









- sw.js

```
// 캐싱 스토리지에 저장될 이름
var CACHE_NAME = "cache-v1";
// 캐싱할 웹 리소스(이미지, css..) 목록
var filesToCache = [
  "/",
  "/favicon.ico",
  "/img/Google_Chrome.png",


  // 캐싱할 파일들 추가..
];

// Service Worker install(웹 자원 캐싱)
self.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        // pwa 파일에 전부 넣기
        return cache.addAll(filesToCache);
    })
    .catch(function(err) {
      return console.log(err);
    })
  );
});

// fetch
self.addEventListener("fetch", function(event) {
  event.respondWith(
    caches.match(event.request)
    .then(function(response) {
      return response || fetch(event.request);
    })
    .catch(function(err) {
      return console.log(err)
    })
  );
});

// activate
self.addEventListener("fetch", function(event) {
  var newCacheList = ["cache-v1"];

  event.waitUntil(
    caches.keys()
    .then(function(cacheList) {
      return Promise.all(
        cacheList.map(function(cacheName) {
          if (newCacheList.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      )
    })
    .catch(function(err) {
      return console.log(err)
    })
  );
});

```

