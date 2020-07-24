# Linked List-1



![](img/Linked List.png)


<br>

## 구조

- 연결 리스트라고도 함

- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조

- 링크드 리스트는 떨어진 곳에 존재하는 데이터를 연결해서 관리하는 데이터 구조

- 본래 C언어에서는 주요한 데이터 구조이지만 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원



<br>



### 기본 구조와 용어

- 노드(Node): 데이터 저장 단위(데이터값, 포인터)로 구성
- 포인터(pointer): 각 노드 안에서 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간



<br>



## 간단한 링크드 리스트 예

### Node 구현

- 보통 파이썬에서 링크드 리스트 구현시 파이썬 클래스를 활용함
  - 파이썬 객체지향 문법 이해 필요
  - www.fun-coding.org/



- 구현

```
class Node:
	def __init__(self, data):
	self.data = data
	self.next = None
```



```
Class Node:
	def __init__(self, data, next=None):
	self.data = data
	self.next = next
```

<br>

두 코드의 차이

인자가 한개인지 두개인지..

인자를 하나만 넣어주면 next는 None으로 default됨



<br>

### Node와 Node 연결하기



```
node1 = Node(1)
node2 = Node(2)
# 두 객체간에 연결은 아직 안됨

# 연결
node1.next = node2
head = node1	# 가장 앞에 있는것이 node1 이다
```



<br>

### 링크드 리스트로 데이터 추가하기

```
class None:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
		
def add(data):
	node = head
	# 맨 끝은 찾아야 함
	# 이 노드의 다음 주소를 나타내는게 있다면 다음 노드로 이동
	# 다음 노드의 주소가 없다면 이 노드가 마지막 노드이다
	while node.next:
		node = node.next
	# 마지막 노드에게 새로운 노드를 연결
	node.next = Node(data)
```



```
node1 = Node(1)
head = node1
for index in range(1, 10):
	add(index)

```



<br>

### 링크드 리스트 데이터 출력하기(검색하기)

```
node = head
while node.next:
	print(node.data)	# 순회
	node = node.next
print(node.data)
```

