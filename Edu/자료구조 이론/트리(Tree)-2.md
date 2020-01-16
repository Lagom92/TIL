# 트리(Tree) - 2

<br/>

## 5. 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

<br/>

### 5.1. 노드 클래스 만들기

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```



<br/>

### 5.5. 이진 탐색 트리에 데이터 넣기

- 이진 탐색 트리 조건에 부합하게 데이터를 넣어야 함

```python
class NoneMgmt:
    def __init__(self, head):
        self.head = head
        
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
                
```





---ing





