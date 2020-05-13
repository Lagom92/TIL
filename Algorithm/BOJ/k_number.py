# 백준 11004번 K번째 수
# https://www.acmicpc.net/problem/11004
'''
오름차순으로 정렬했을때, K 번째 있는 수 구하기
'''


N, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
    
print(num_list[K-1])