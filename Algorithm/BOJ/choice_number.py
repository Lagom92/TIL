# 백준 2230번 수 고르기
# https://www.acmicpc.net/problem/2230
'''

미완
'''


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

print(n, m)
print(arr)

a, b = 0, 0
res = arr[-1] - arr[0]

while True:
    val = arr[b] - arr[a] 
    if val < m:
        b += 1
    else:
        if val < res:
            res = val
            a += 1

    if a == n-1 or b == n-1:
        break

print(res)

    
