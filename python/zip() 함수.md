# Zip() 함수



### zip(*iterable)

동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수



```python
list(zip([1,2,3], [4,5,6]))
```

```python
[(1, 4), (2, 5), (3, 6)
```



```python
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
```

```
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```



```python
list(zip("abc", "def"))
```

```python
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```



```python
a = [1, 2, 3]
b = "abc"

for x, y in zip(a, b):
	print(x, y)
```

```python
# 출력
1 a
2 b
3 c
```



- 리스트나 문자열들의 갯수가 맞지 않은 경우 해당 값은 출력되지 않는다.

```python
a = [1, 2, 3, 4, 5]
b = "abc"

for x, y in zip(a, b):
	print(x, y)
```

```python
# 출력
1 a
2 b
3 c
```





### 서로 길이가 다른 list에 zip() 적용하기

- zip() 함수를 사용하는데 리스트들의 길이가 서로 다르면 일반적으로 위의 경우처럼 생략되어서 출력이 된다.
- 하지만 `itertools.zip_longest()`를 사용하면 해결 할 수 있다.

```
from itertools import zip_longest

a = [1, 2, 3, 4, 5]
b = ["a","b", "c"]

res = list(zip_longest(a, b))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]

res = list(zip_longest(a, b, fillvalue=0))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 0), (5, 0)]
```

`fillvalue`를 이용해서 None대신 값을 넣어 줄 수 가 있다.





### dictionary의 최대값, 최소값 찾기

- Dictionary의 {key: value} 중 value 값으로 최대값과 최소값 찾기

```
# zip()를 이용해서 dic의 value값 기준의 최대 최소 찾기

dic = {
    "Kim": 19,
    "Yang": 24,
    "Han": 22
	}
# {'Kim': 19, 'Yang': 24, 'Han': 22}

min_dic = min(list(zip(dic.values(), dic.keys())))
# (19, 'Kim')

max_dic = max(list(zip(dic.values(), dic.keys())))
# (24, 'Yang')
```











----------------------------------------



### 참고

https://wikidocs.net/32#zip

https://excelsior-cjh.tistory.com/100

https://docs.python.org/3/library/functions.html#zip