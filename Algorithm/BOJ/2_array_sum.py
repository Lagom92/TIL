# 백준 2167번 2차원 배열의 합
# https://www.acmicpc.net/problem/2167
'''
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합

'''

# python으로 실행하면 시간 초과 발생
# pypy3로 실행하면 통과함
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    res = 0
    for col in range(i-1, x):
        for row in range(j-1, y):
            res += arr[col][row]
    
    print(res)



# 다른 사람 풀이
# DP 사용 