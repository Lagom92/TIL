# 백준 17389번 보너스 점수
# https://www.acmicpc.net/problem/17389

N = int(input())
S = input()
score = 0
bonus = 0

for i in range(N):
    if S[i] == 'O':
        score += (i+1)
        score += bonus
        bonus += 1
    else:
        bonus = 0

print(score)