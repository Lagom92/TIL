# 백준 11055번 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11055
'''
수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력

test case
10
1 100 2 50 60 3 5 6 7 8

ans: 113
'''

import copy

n = int(input())
seq = list(map(int, input().split()))

dp = copy.deepcopy(seq)

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], seq[i] + dp[j])

print(max(dp))

