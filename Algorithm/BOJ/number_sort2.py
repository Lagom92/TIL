# 백준 2751번 수 정렬하기2
# https://www.acmicpc.net/problem/2751
'''
input() 대신 sys.stdin.readline() 사용해야 시간 초과가 발생 하지 않음
'''

import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]

num_list.sort()

for i in num_list:
    print(i)




# 다른 사람 코드

