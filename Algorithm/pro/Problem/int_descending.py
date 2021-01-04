# 프로그래머스 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933
'''
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴

입출력 예
n	return
118372	873211
'''

def solution(n):
    answer = ''
    lst_n = list(str(n))
    set_n = sorted(set(str(n)), reverse=True)
    for i in set_n:
        cnt = lst_n.count(i)
        for _ in range(cnt):
            answer += i

    return int(answer)



# 다른 사람 코드
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)

    return int("".join(ls))
