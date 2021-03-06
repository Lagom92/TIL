# 힙(Heap) - 2

<br/>

## 3. 힙(Heap) 동작

- 데이터를 힙 구조에 삽입, 삭제하는 과정을 그림을 통해 선명하게 이해하기



<br/>

### 힙에 데이터 삽입하기 - 기본동작

- 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입



<br/>

#### Heap 동작 gif

![](./img/heap sort.gif)



<br/>

완전 이진 트리에 맞게 데이터가 들어오면 입력한다.

데이터가 들어 온 후

최대힙의 경우, 부모 노드와 비교하여 부모 노드 보다 작으면 자리를 바꿔준다.



<br/>

### 힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap의 경우)

- 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
- 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함(swap)



<br/>

### 힙 데이터 삭제하기 (Max Heap의 경우)

- 보통 삭제는 최상단 노드(root 노드)를 삭제하는 것이 일반적임
  - 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
- 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드(일반적으로 가장 마지막에 추가한 노드)를 root 노드로 이동
- root 노드의 값이 child node 보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함



-ing



<br/>

