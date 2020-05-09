# 백준 2750번 수 정렬하기
# https://www.acmicpc.net/problem/2750
'''
N개의 수가 주어질때, 오름차순으로 정렬하기
'''
# sort() 사용
N = int(input())
numbers = list(int(input()) for _ in range(N))
numbers.sort()
for i in numbers:
    print(i)



# 다른 사람 코드 
# 선택 정렬 알고리즘
n = int(input())
array = list(int(input()) for _ in range(n))
for i in range(n):
    min_idx = i     # 가장 작은 원소의 인덱스
    for j in range(i+1, n):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

for i in array:
    print(i)