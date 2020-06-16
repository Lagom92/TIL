# 프로그래머스 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
'''
포인트
짝수는 제외
set의 차집합 이용

test case
n	result
10	4
5	3
'''


def solution(n):
    res = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in res:
            res -= set(range(i*2, n+1, i))
    
    return len(res)


n = 5
print(solution(n))