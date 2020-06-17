# 프로그래머스 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915
'''
주어진 인덱스 n의 값을 이용해서 정렬하기

사전순으로 정렬

테스트 케이스
strings	n	return
[sun, bed, car]	1	[car, bed, sun]
[abce, abcd, cdx]	2	[abcd, abce, cdx]
'''

def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings



# 다른 사람 코드
# sort()를 사용 안 한 버전
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''

    min = []
    result = []
    for i in strings:
        min.append(i[n])
        sorted_min = sorted(min)

    while len(result) != len(strings):
        for j in range(0, len(strings)):
            for k in range(0, len(strings)):
                if sorted_min[j] in strings[k][n]:
                    index = k
                    result.append(strings[index])
                    continue

    return result