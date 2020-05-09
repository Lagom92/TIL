# 백준 10814번 나이순 정렬
# https://www.acmicpc.net/problem/10814
'''
이름과 나이가 입력으로 들어올때, 나이순으로 정렬하기

tuple() 과 sort()의 key 옵션을 이용함
'''

N = int(input())
members = []
for _ in range(N):
    datas = input().split()
    members.append((int(datas[0]), datas[1]))

members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])