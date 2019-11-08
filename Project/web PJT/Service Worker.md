# Service Worker



## Web Worker

스크립트를 백그라운드에서 동작되게 하는것



- 쓰레드 ?



- 쓰레드 비슷
- 배그라운드
- 메세지 전달



web worker의 rule

자체적인 글로벌 스코프를 가짐





index.html

```
<!-- serviceWorker -->
     <script type="text/javascript">
       if ("serviceWorker" in navigator) {
         navigator.serviceWorker.register("sw.js").then((reg) => {
           // :)
         }).catch(function(err) {
           // :)
         })
       }
     </script>
```





sw.js

```
self.addEventListener('install', function(event) {
    console.log('[Service Worker] Install');
    
    event.waitUntil(
    // cache-v1이라는 이름으로 Cache Storage를 생성하고,
    caches.open('cache-v1').then(function(cache) {
    return cache.addAll([
    '/',
    '/index.html',
    '/mainfest.json',
    ...
    ])
    })
    )
    
    self.skipWaiting();
    
    console.log('SW installed', event);	
    
});


self.addEven
```

















----



참고

[유튜브 동영상](https://www.youtube.com/watch?v=psQWcltlmqY)