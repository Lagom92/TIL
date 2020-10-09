# 백준 1495번 기타리스트
# https://www.acmicpc.net/problem/1495
'''
모든 볼륨에 대해서 연주 가능 여부를 계산

연주가 가능하면 1, 불가능이면 0

test case
3 5 10
5 3 7

위의 경우 - 표
0 1 2 3 4 5 6 7 8 9 10
0 0 0 0 0 1 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 1 0 0 0
1 0 0 0 0 0 0 0 0 0 1
'''

n, s, m = map(int, input().split())
lst = list(map(int, input().split()))

DP = [ list(0 for _ in range(m+1)) for _ in range(n+1)]
DP[0][s] = 1

for i in range(n):
    v = lst[i]
    for j in range(m+1):
        if DP[i][j] == 1:
            if 0 <= j + v <= m:
                DP[i+1][j+v] = 1
            if 0 <= j - v <= m:
                DP[i+1][j-v] = 1
res = -1
for dp in range(m+1):
    if DP[n][dp] == 1:
        if res < dp:
            res = dp
print(res)
