# 백준 15969번 행복
# https://www.acmicpc.net/problem/15969
'''
최대 점수와 최소 점수의 차이 구하기

max(), min() 함수 사용하여 차이 구하기
or
정렬하여 -1번째와 0번째의 차이 구하기
'''

# 방법 1
N = int(input())
scores = list(map(int, input().split()))
res = max(scores) - min(scores)
print(res)


# 방법 2
N = int(input())
scores = list(map(int, input().split()))
scores.sort()
res = scores[-1] - scores[0]
print(res)