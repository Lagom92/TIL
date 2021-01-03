# 프로그래머스 2xn 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3
'''
피보나치 수열
'''


def solution(n):
    num = 1000000007
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b%num, (a+b)%num
    return b

n = 4   # result: 5
result = solution(n)
print(result)
