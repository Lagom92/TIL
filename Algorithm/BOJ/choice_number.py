# 백준 2230번 수 고르기
# https://www.acmicpc.net/problem/2230
'''
1. 정렬
2. a, b 포인터 두개 만들기
3. 차이값이 m보다 크면 a++
    차이값 중 최소인 값 저장(res)
4. 차이값이 m보다 작으면 b++
'''

# 방법 1 - 시간초과
'''
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

res = 1000000000
for i in range(n):
    for j in range(i, n):
        val = abs(arr[i] - arr[j])
        if val >= m:
            if val < res:
                res = val
print(res)
'''


# 방법 2 - 성공
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

a, b = 0, 0
res = float('inf')

while a < n and b < n:
    val = abs(arr[a] - arr[b])
    if val >= m:
        a += 1
        if val < res:
            res = val
    else:
        b += 1

print(res)
