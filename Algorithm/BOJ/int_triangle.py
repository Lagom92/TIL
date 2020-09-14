# 백준 1932번 정수 삼각형
# https://www.acmicpc.net/problem/1932
'''
DP 사용

test case
3
7
3 8
8 1 0
'''


n = int(input())
res = [0] * (n+1)

for i in range(n):
    nums = [0] + list(map(int, input().split())) + [0]
    for j in range(1, i+2):
        maxV = max(res[j], res[j-1])
        nums[j] += maxV
    res = nums[::]

print(max(res))
