# 백준 1915번 가장 큰 정사각형
# https://www.acmicpc.net/problem/1915
'''
DP 이용

점화식
MAP[i][j] = Min(MAP[i - 1][j - 1] , Min(MAP[i - 1][j], MAP[i][j - 1])) + 1 
'''

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _  in range(n)]
DP = [list(0 for _ in range(m+1)) for _ in range(n+1)]
res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            DP[i][j] = min(DP[i-1][j-1], DP[i][j-1], DP[i-1][j]) + 1
            res = max(DP[i][j], res)

print(res**2)
