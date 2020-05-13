# 백준 1568번 새
# https://www.acmicpc.net/problem/1568

N = int(input())
i = 0
cnt = 0

while N:
    i += 1
    if i > N:
        i = 0
    else:
        N -= i
        cnt += 1
print(cnt)