# 백준 2003번 수들의 합 2
# https://www.acmicpc.net/problem/2003
'''

two pointers 사용

s 와 e 두개의 포인터를 사용해서 합을 계산함

'''

# 방법 1 - 시간 초과 발생함
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(N):
    for j in range(i, N):
        if sum(arr[i:j+1]) == M:
            res += 1
print(res)
'''


# 방법 2 성공 - 투 포인터 사용
N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
s, e = 0, 0

while e < N:
    sum_lst = sum(arr[s:e+1])
    if sum_lst == M:
        res += 1
        e += 1
    elif sum_lst < M:
        e += 1
    else:
        s += 1
    
print(res)
