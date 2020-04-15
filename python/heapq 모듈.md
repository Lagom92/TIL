# heapq 모듈

<br/>

### heap ?

- 완전 이진 트리를 기본으로 한 자료 구조

- 자료 구조 형태 중 하나로서 우선순위 큐를 위해 만들어진 구조이다.

- 코딩 테스트 문제 중 최소값, 최대값을 계속해서 호출해야 하는 경우 heap 구조를 이용하여 구현하면 시간 측면에서 효율적인 구현이 가능하다.



<br/>

### heapq ?

- 우선순위 큐 알고리즘이라고 하는 힙(heap) 큐 알고리즘의 구현을 제공

- 파이썬의 리스트를 최소 힙처럼 사용할 수 있게 하는 것



<br/>

### import heapq

- heapq는 내장모듈로서 따로 설치가 필요하지 않다.

<br/>

```
import heapq
```



<br/>

### Using heapq

- 기존 배열(리스트)을 heap 구조로 만들기_**heapify()**

```python
my_heap = [1, 3, 2, 6, 8, 0, 6]
heapq.heapify(my_heap)
print(my_heap)

# [0, 3, 1, 6, 8, 2, 6]
```

<br/>

- heap에 요소 추가하기_**heappush(배열이름, 요소)**

```python
my_heap = []
heapq.heappush(my_heap, 3)
heapq.heappush(my_heap, 5)
heapq.heappush(my_heap, 1)
heapq.heappush(my_heap, -3)
print(my_heap)

# [-3, 1, 3, 5]
```

<br/>

- heap 요소 제거하기_**heappop(배열이름)**

```python
my_heap = []
heapq.heappush(my_heap, 3)
heapq.heappush(my_heap, 5)
heapq.heappush(my_heap, 1)
heapq.heappush(my_heap, -3)
print(my_heap)

heapq.heappop(my_heap)
heapq.heappop(my_heap)
print(my_heap)

# [-3, 1, 3, 5]
# [3, 5]
```



<br/>

### 최소값 찾을때 주의!

- heapq는 모든 원소를 하나하나 정렬하는 것은 아니다.
- my_heap[0]가 해당 리스트의 최소값은 맞지만 my_heap[1]가 두번째로 작은 원소라고는 할 수 없다.

```python
import heapq

my_heap = [1, 3, 2, 6, 8, 0, 6]
heapq.heapify(my_heap)
print(my_heap)

print(my_heap[0])
print(my_heap[1])

# [0, 3, 1, 6, 8, 2, 6]
# 0
# 3
```

<br/>

- 두번째 작은 값을 찾고 싶다면 heapq.heappop()를 사용해서 가장 작은 원소를 제거 한 후 my_heap[0]를 찾아야 한다.

```python
my_heap = [1, 3, 2, 6, 8, 0, 6]
heapq.heapify(my_heap)
print(my_heap)

print(my_heap[0])

heapq.heappop(my_heap)
print(my_heap[0])

# [0, 3, 1, 6, 8, 2, 6]
# 0
# 1
```











<br/><br/>

--------------------

### Reference

-  https://python.flowdas.com/library/heapq.html 

-  https://www.daleseo.com/python-heapq/ 
-  https://www.daleseo.com/python-heapq/ 

<br/>

