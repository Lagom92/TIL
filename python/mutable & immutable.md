# mutable & immutable



- mutable

값이 변한다는 뜻

변할 수 있는

리스트(List), 딕셔너리(Dictionary), 세트(Set)



- immutable

값이 변하지 않는다는 뜻

변할 수 없는

숫자형(Number), 문자열(String), 튜플(Tuple), 







-------------



- 문자열의 경우(immutable)

```
>>> abc = 'abcd'
>>> id(abc)
2096192935224
>>> abc + 'd'
'abcdd'
>>> abc		# abc의 값이 변경 X
'abcd'
>>> id(abc)		# 객체 변경 X
2096192935224
```



- 리스트의 경우(mutable)

````
>>> box = ['a', 'b', 'c']
>>> box
['a', 'b', 'c']
>>> id(box)
2096192915080
>>> box.append('d')
>>> box		# 값 변경
['a', 'b', 'c', 'd']
>>> id(box)		# 객체 변경 X
2096192915080
````



- 데이터 타입에 mutable과 immutable이 있는 이유 ??

성능적인 이점 때문

코딩을 할때 값을 자주 변경해야하는 데이터가 있을 수있다. 이때 immutable을 이용하면 객체가 계속 생성되면서 메모리에 부담을 줄 수 있다. 이럴때 mutable을 사용하면 메모리 사용의 효율을 높일 수 있다.



