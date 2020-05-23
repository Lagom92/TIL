# 백준 1920번 수 찾기
# https://www.acmicpc.net/problem/1920
'''
M_list에 있는 값이 N_list에 있는지 확인하는 코드

N_list를 list()로 할 경우 시간초과가 발생함
set()으로 하면 시간초과가 해결됨 
'''

N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)



# 다른 사람 코드
N, A = int(input()), {i:1 for i in map(int, input().split())}
M = int(input())

for i in list(map(int, input().split())):
    print(A.get(i, 0))