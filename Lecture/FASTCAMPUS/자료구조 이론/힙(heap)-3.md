# 힙(Heap) - 3

<br/>

## 4. 힙 구현

### 힙과 배열

- 일반적으로 힙 구현시 배열 자료구조를 활용함
- 배열은 인덱스가 0부터 시작하지만,  힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀 더 수월함
  - 부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호(child node's index) // 2
  - 왼쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2
  - 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2 + 1



<br/>

![](./img/heap_index.png)





-ing





<br/>

<br/>

----------------------

<br/>

### Reference

- https://www.geeksforgeeks.org/binary-heap/