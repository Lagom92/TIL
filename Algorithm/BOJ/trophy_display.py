# 백준 1668번 트로피 진열
# https://www.acmicpc.net/problem/1668
'''

현 위치에서 앞 쪽에 있는 것들 중 가장 큰 것 보다 현재 데이터의 크기가 커야함
'''
def solution(n, trophy_list):
    cnt = 1
    maxV = trophy_list[0]
    for i in range(1, n):
        if trophy_list[i] > maxV:
            cnt += 1
        if maxV < trophy_list[i]:
            maxV = trophy_list[i]
    return cnt


N = int(input())
trophy_list = list(int(input()) for _ in range(N))

left = solution(N, trophy_list)
right = solution(N, trophy_list[::-1])

print(left)
print(right)