# 백준 1439번 뒤집기
# https://www.acmicpc.net/problem/1439
'''
1 => 0 으로 또는 0 => 1으로 변경하는것

포인트
첫번째 값이 무엇인지(0 or 1)
1에서 0으로 바뀌거나 0에서 1로 바뀌는 횟수
'''

S = input()

print(S)

# 전부 0로 만드는 경우
cnt0 = 0
# 전부 1로 만드는 경우
cnt1 = 0

# 첫 번째 값을 바꿔주는 것
if S[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:  # 지금과 다음꺼를 비교
        if S[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))