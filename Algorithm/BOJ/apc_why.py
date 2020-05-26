# 백준 17224번 APC는 왜 서브테스크 대회가 되었을까?
# https://www.acmicpc.net/problem/17224
'''

어려운것(140점)들을 풀고 문제를 더 풀수 있으면 쉬운 문제(100점)를 푼다.
'''

# 부분 성공
N, L, K = map(int, input().split())
res = 0
cnt = 0
sub_list = []
rest_list = []
for i in range(N):
    sub1, sub2 = map(int, input().split())
    sub_list.append((sub1, sub2))

sub_list.sort(key=lambda x: x[1])
while sub_list:
    sub = sub_list.pop(0)
    if sub[1] <= L:
        cnt += 1
        res += 140
    else:
        rest_list.append(sub)
    if cnt >= K:
        break

if cnt < K:
    rest_list.sort()
    while rest_list:
        sub = rest_list.pop(0)
        if sub[0] <= L:
            cnt += 1
            res += 100
        if cnt >= K:
            break

print(res)
    


# 다른 사람 코드_성공
N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# 어려운 문제 점수
ans = min(hard, K)*140

# easy
if hard < K:
    ans += min(K-hard, easy)*100

print(ans)
