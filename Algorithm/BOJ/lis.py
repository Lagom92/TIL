# 백준 11053번 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
'''
DP, 가장 긴 증가하는 부분 수열(LIS)

dp[i] = sequence[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
모든 0 <= j <= i에 대하여, dp[i] = max(dp[i], dp[j]+1) if sequence[j] < sequence[i]

추가 test case
8
1 5 10 3 13 18 15 16
ans: 6
'''

# 다른 사람 코드 참고
N = int(input())
sequence = list(map(int, input().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(0, i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))