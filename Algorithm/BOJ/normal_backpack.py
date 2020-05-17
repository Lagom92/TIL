# 백준 12865번 평범한 배낭
# https://www.acmicpc.net/problem/12865
'''
물건의 개수: N, 최대 무게: K

모든 무게에 대하여 최대 가치를 저장하기

D[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치

각 물품의 번호 i에 따라서 최대 가치 테이블 D[i][j]를 갱신하여 문제를 해결
'''

# 다른 사람 코드 참고함
n, k = map(int, input().split())
dp = list([0]*(k+1) for _ in range(n+1))

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])