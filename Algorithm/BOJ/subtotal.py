# 백준 1806번 부분합
# https://www.acmicpc.net/problem/1806
'''
two pointers 사용

sum()을 미리 계산해둔것을 사용
'''


# 방법 1 - 시간초과 발생함
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))

# res = float('inf')
# left, right = 0, 0

# while left != n:
#     val = arr[left:right+1]
#     if sum(val) >= s:
#         if right-left+1 < res:
#             res = right-left+1
#         left += 1
#     else:
#         if right != n:
#             right += 1
#         else:
#             left += 1

# if res == float('inf'):
#     print(0)
# else:
#     print(res)



# 방법 2 - 성공
n, s = map(int, input().split())
arr = list(map(int, input().split()))

lst = [0]*(n+1)
for i in range(1, n+1):
    lst[i] = lst[i-1] + arr[i-1]

res = 1000001
left, right = 0, 1

while left != n:
    if lst[right] - lst[left] >= s:
        if right-left < res:
            res = right-left
        left += 1
    else:
        if right != n:
            right += 1
        else:
            left += 1

if res == 1000001:
    print(0)
else:
    print(res)