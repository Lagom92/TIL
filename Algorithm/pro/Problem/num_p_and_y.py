# 프로그래머스 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916
'''
p 와 y의 개수가 같은지 체크하는 문제

대소문자 구별 X
'''

def solution(s):
    s = s.upper()
    num_p, num_y = 0, 0
    for i in s:
        if i == 'P':
            num_p += 1
        elif i == 'Y':
            num_y += 1
    if num_p == num_y:
        return True
    else:
        return False



# 다른 사람 코드
'''
lower()를 이용해서 소무자로 변경
count()를 이용해서 개수 계산
'''
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

print( numPY("pPoooyY") )
print( numPY("Pyy") )