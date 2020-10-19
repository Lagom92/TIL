# 백준 11441번  합 구하기
# https://www.acmicpc.net/problem/11441
'''
prefix sum 사용

input() 대신에 sys.stdin.readline() !!!!!!!!
'''

import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

prefix_sum = [0]*(N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    res = prefix_sum[j] - prefix_sum[i-1]
    print(res)
    