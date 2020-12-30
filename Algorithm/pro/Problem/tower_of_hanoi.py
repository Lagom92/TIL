# 프로그래머스 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946
'''
'''


def hanoi(n, fr, tem, to, answer):
    if n == 1:
        answer.append([fr, to])
    else:
        hanoi(n-1, fr, to, tem, answer)
        answer.append([fr, to])
        hanoi(n-1, tem, fr, to, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer


n = 1
print(solution(n))
