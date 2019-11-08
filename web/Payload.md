# Payload



- Notification을 이용한 push라는 것에 대해 공부하던 중 처음 알게 되었다.



```
messaging.onMessage(function(payload) {
  var title = payload.notification.title;
  var options = {
    body: payload.notification.body,
    icon: payload.notification.icon
  };
  new Notification(title, options);
});
```





> The term ‘payload’ is used to distinguish between the ‘interesting’ information in a chunk of data or similar, and the overhead to support it. It is borrowed from transportation, where it refers to the part of the load that ‘pays’: for example, a tanker truck may carry 20 tons of oil, but the fully loaded vehicle weighs much more than that – there’s the vehicle itself, the driver, fuel, the tank, etc. It costs money to move all these, but the customer only cares about (and pays for) the oil, hence, ‘pay-load’.
>
> In programming, the most common usage of the term is in the context of message protocols, to differentiate the protocol overhead from the actual data.
>
> 
>
> 출처: 
>
> [What does the term 'Payload' mean in Programming](https://softwareengineering.stackexchange.com/questions/158603/what-does-the-term-payload-mean-in-programming)
>
> 



- 위키백과에 한글로 번역된 글이 있었다.



> 페이로드라는 용어는 큰 데이터 덩어리 중에 '흥미 있는' 데이터를 구별하는 데 사용된다. 이 용어는 운송업에서 비롯하였는데, 지급(pay)해야 하는 적화물(load)을 의미한다. 예를 들어, 유조선 트럭이 20톤의 기름을 운반한다면 트럭의 총 무게는 차체, 운전자 등의 무게 때문에 그것보다 더 될 것이다. 이 모든 무게를 운송하는데 비용이 들지만, 고객은 오직 기름의 무게만을 지급(pay)하게 된다. 그래서 'pay-load'란 말이 나온 것이다.
>
> 프로그래밍에서 주로 메시지 프로토콜(message protocols) 중에 프로토콜 오버헤드(protocol overhead)와 원하는 데이터를 구별할 때 사용된다
>
> 
>
> 출처:
>
> [위키백과(페이로드)](https://ko.wikipedia.org/wiki/%ED%8E%98%EC%9D%B4%EB%A1%9C%EB%93%9C_(%EC%BB%B4%ED%93%A8%ED%8C%85))
>
> 