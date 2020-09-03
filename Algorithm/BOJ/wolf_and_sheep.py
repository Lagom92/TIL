# 백준 16956번 늑대와 양
# https://www.acmicpc.net/problem/16956

'''
키포인트

예시 출력과 똑같은 출력을 만들지 않아도 된다.
그냥 1인지 0인지 출력하고
그에 따른 목장의 모양만 출력 하면 된다.
즉, 양과 늑대가 있는 곳을 빼고 전부 울타리로 만들어도 통과된다.

늑대의 사방을 탐색해서 양이 있으면 0 리턴
울타리를 만들 수 있는 곳에는 울타리 만들기
끝나면 1 리턴
'''

r, c = map(int, input().split())

field = [list(input()) for _ in range(r)]

def find_sheep(r, c, field):
    x = [1, 0, -1, 0]
    y = [0, -1, 0, 1]

    for i in range(r):
        for j in range(c):
            if field[i][j] == 'W':
                for k in range(4):
                    kx = i + x[k]
                    ky = j + y[k]
                    if 0 <= kx <= r-1 and 0 <= ky <= c-1:
                        if field[kx][ky] == 'S':
                            return 0
                
            elif field[i][j] == '.':
                field[i][j] = 'D'
    
    return 1


res = find_sheep(r, c, field)
print(res)
if res:
    for i in range(r):
        print(''.join(field[i]))
