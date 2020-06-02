# 백준 1074번 Z
# https://www.acmicpc.net/problem/1074

'''
나중에 다시 풀기

배열의 크기: 2^N * 2^N
0 <= r, c <= 2^N-1

Z: (0,0)을 기준으로 x, y의 숫자

(0,0) (0,1) (1,0) (1,1)
0, 1, 2, 3
=> i*2+j
'''

N, r, c = map(int, input().split())

def Z(size, x, y):
    if size == 1:
        return 0
    size //= 2
    for i in range(2):
        for j in range(2):
            if x < size*(i+1) and y < size*(j+1):
                return (i*2+j) * size*size + Z(size, x-size*i, y-size*j)


print(Z(2**N, r, c))