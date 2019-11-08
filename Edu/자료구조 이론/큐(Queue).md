# 큐(Queue)



FIFO

First in First out

가장 먼저 넣는 데이터를 가장 먼저 꺼낼 수 있는 구조

큐 = 한줄 서기

먼저 들어온게 먼저 나간다.





- 알아둘 용어

Enqueue: 큐에 데이터를 넣는 기능

Dequeue: 큐에서 데이터를 꺼내는 기능





- 파이썬 라이브러리 queue

Queue(): 가장 일반적인 큐 자료 구조

LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조라고 보면 됨)

PriorityQueue(): 데이터마다 우선순위를 넣어서 우선순위가 높은 순으로 데이터 출력





- Queue()

```python
import queue

data_queue = queue.Queue()	# 일반적인 큐

data_queue.put('data')	# Enqueue
data_queue.put(1)	# Enqueue

data_queue.qsize()	# 큐의 사이즈 

data_queue.get()	# Dequeue
```





- LifoQueue()

```python
# Last in First out
import queue

data_queue = queue.LifoQueue()

data_queue.put('data')
data_queue.put(1)

data_queue.qsize()	# 2가 출력됨

data_queue.get()	# 1이 출력됨
```





- PriorityQueue()

```python
# 우선순위에 따라서 출력
import queue

data_queue = queue.PriorityQueue()

data_queue.put((10, 'data'))	# 튜플로 (우선순위, data) 입력
data_queue.put((5, 2))
data_queue.put((20, 100))

data_queue.qsize()

data_queue.get()	# (5, 2) 
data_queue.get()	# (10, 'data')
```





- 큐가 많이 사용되는 곳 ?

멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨(운영체제 참조)

큐의 경우에는 장단점 보다는 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음



>이 부분은 이해가 않된다.
>
>추가 공부가 꼭 필요해 보인다.





- 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현

```python
queue_list = list()

def enqueue(data):
	queue_list.append(data)
	
def dequeue(data):
	data = queue_list[0]
    del queue_list[0]	# 해당 리스트의 첫번째 제거
    return data
```

```python
for i in range(10):
	enqueue(i)
	
len(queue_list)	# 10

dequeue()	# 0
```

