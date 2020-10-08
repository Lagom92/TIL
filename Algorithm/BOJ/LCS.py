# 백준 9251번 LCS
# https://www.acmicpc.net/problem/9251
'''
LCS 알고리즘 

test case
ACAYKP
CAPCAK
'''

s1 = input()
s2 = input()

DP = [list(0 for _ in range(len(s2) + 1)) for _ in range(len(s1) + 1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            DP[i+1][j+1] = DP[i][j] + 1
        else:
            DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])

print(DP[-1][-1])