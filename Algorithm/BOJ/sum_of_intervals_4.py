# 백준 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659


# 방법 1 - 시간초과
'''
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())
    print(sum(numbers[i-1:j]))
'''


# 방법 2 - 성공
'''
prefix sum 사용

그런데 백준에서 코드를 돌려보니 시간초과가 발생했다.

이유를 찾아보니 

input() 대신 sys.stdin.readline()을 사용해야 한다.
'''

import sys

# input() 대신 sys.stdin.readline()

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]*(N+1)
for i in range(N):
    num = prefix_sum[i] + numbers[i]
    prefix_sum[i+1] = num

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    res = prefix_sum[j] - prefix_sum[i-1]
    print(res)
