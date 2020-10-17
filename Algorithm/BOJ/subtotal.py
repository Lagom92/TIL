# 백준 1806번 부분합
# https://www.acmicpc.net/problem/1806
'''
'''

# 방법 1 - 시간초과 발생함
n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

res = float('inf')
a, b = 0, 0

while True:
    val = sum(arr[a:b+1])
    if val >= s:
        length = b - a + 1
        if length < res:
            res = length
        a += 1
    else:
        b += 1

    if a == n-1 and b == n-1:
        break

print(res)