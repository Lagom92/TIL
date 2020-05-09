# 백준 11650번 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
'''
tuple에 sort()를 할 경우
기본적으로 튜플의 인덱스 순서대로 오름차순으로 정렬하게 된다.
'''

N = int(input())
location = []

for _ in range(N):
    location.append(tuple(map(int, input().split())))

location.sort()

for i in location:
    print(i[0], i[1])