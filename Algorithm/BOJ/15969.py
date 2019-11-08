# BOJ
# 15969번 문제 행복
'''
숫자의 갯수 N
점수들의 리스트 scores

점수 리스트를 정렬하고난 후 
가장 큰 [-1] 에서  가장작은 [0]을 빼주었다.
'''
N = int(input())
scores = list(map(int, input().split()))

scores = sorted(scores)
print(scores[-1] - scores[0])

'''
다른 풀이 방법
'''
print("다른 풀이")

N, lst = int(input()), list(map(int, input().split()))
print(max(lst) - min(lst))