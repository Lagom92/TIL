# 프로그래머스 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645
'''
'''

def solution(n):
    arr = list([0 for _ in range(n)] for _ in range(n))
    # print(arr)
    x, y = -1, 0
    num = 1
    res = []
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:    # down
                x += 1
            elif i%3 == 1:  # right
                y += 1
            elif i%3 == 2:  # up
                x -= 1
                y -= 1

            arr[x][y] = num
            num += 1

    # print(arr)
    for i in range(n):
        for j in range(i+1):
            res.append(arr[i][j])
    
    return res

n = 4
print("RES: ", solution(n))