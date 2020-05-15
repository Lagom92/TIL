# 백준 1904번 01타일
# https://www.acmicpc.net/problem/1904
'''
DP

N이 1일때, 2일때, ...를 손으로 적어보면 
개수가 1, 2, 3, 5, ....
즉 피보나치 수열이 나온다.
'''

N = int(input())

dp = [0]*1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])