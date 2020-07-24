# 트리(Tree)-3

### 5.3. 이진 탐색 트리 검색(search)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            # 왼쪽
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break

            # 오르쪽
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            # 현재값이 찾는 값일 경우
            if self.current_node.value == value:
                return True
            # 왼쪽
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            # 오른쪽
            else:
                self.current_node = self.current_node.right

        return False
```

<br/>

- Code 확인하기

```python
head = Node(1)
BST = NodeMgmt(head)
BST.insert(22)
BST.insert(3)
BST.insert(4)
BST.insert(5)

print(BST.search(3))
print(BST.search(7))

# True
# False
```







<br/>

<br/>