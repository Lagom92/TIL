# 백준 9037번 The candy war
# https://www.acmicpc.net/problem/9037


T = int(input())
for tc in range(T):
    N = int(input())
    kids = list(map(int, input().split()))
    cnt = 0

    while len(set(kids)) != 1:
        candy_move = []

        # 초기에 홀수는 짝수로 변경, 절반으로 나눔
        for i in range(N):
            if kids[i] % 2 == 1:
                kids[i] += 1
            candy_move.append(kids[i]//2)

        # 모두 같은 수 일 경우 종료
        if len(set(kids)) == 1:
            break

        # 맨 마지막 캔디는 맨 앞의 캔디에 더해짐
        num = candy_move[0] + candy_move[-1]
        if num % 2 == 1:
            num += 1
        kids = [num]

        # 캔디를 옆으로 나눠줌
        for i in range(0, N-1):
            num = candy_move[i] + candy_move[i+1]
            if num % 2 == 1:
                num += 1
            kids.append(num)
        cnt += 1

        # 모두 같은 수 일 경우 종료
        if len(set(kids)) == 1:
            break

    print(cnt)



# 다른 사람 코드
def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    
    return len(set(candy)) == 1


def teacher(N, candy):
    tmp_lst = [0]*N
    for i in range(N):
        if candy[i]%2:
            candy[i] += 1
        candy[i] //= 2
        tmp_lst[(i+1) % N] = candy[i]

    for i in range(N):
        candy[i] += tmp_lst[i]

    return candy 


def candy_war():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for _ in range(int(input())):
    candy_war()