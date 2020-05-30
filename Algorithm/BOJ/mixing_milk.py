# 백준 16769번 Mixing Milk
# https://www.acmicpc.net/problem/16769
'''
우유를 옆으로 전부 부어버리기, 100번 부었을때 우유가 얼마나 들어있는지 출력

우유를 붓는것을 하나의 함수로 구현함
단순하게 100번 부어서 결과를 출력함
'''
capacity = []
milk = []
for _ in range(3):
    c, m = map(int, input().split())
    capacity.append(c)
    milk.append(m)

def milk_pours(a, b):
    global capacity, milk 

    if milk[a] + milk[b] <= capacity[b]:
        milk[b] += milk[a]
        milk[a] = 0
    else:
        milk[a] = (milk[a] + milk[b]) - capacity[b]
        milk[b] = capacity[b]
    return

cnt = 0
while True:
    for i in range(3):
        if i < 2:
            milk_pours(i, i+1)      # 0 -> 1, 1 -> 2
        else:
            milk_pours(i, i-2)      # 2 -> 0
        cnt += 1
        if cnt == 100:
            break
    if cnt == 100:
        break

for i in range(3):
    print(milk[i])



# 다른 사람 코드
'''
포인트
for문을 사용해서 100번만 돌도록함
% 를 이용해서 인덱스를 구함
min(), max()를 이용해서 조건문을 사용하지 않고 원하는 값을 찾음
'''
C, M = [0]*3, [0]*3
for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    idx, nxt = i % 3, (i+1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)