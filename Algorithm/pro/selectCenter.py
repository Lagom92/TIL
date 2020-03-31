# 가운데 글자 가져오기
'''
글자 s의 길이 n을 찾은 후 짝수/홀수 일 때 경우를 생각해서 슬라이싱

input
"abcde"
"qwer"

output
"c"
"we"
'''

def solution(s):
    answer = ''
    n = len(s)
    if n%2:
        idx = n//2
        answer = s[idx]
    else:
        idx = n//2 -1
        answer = s[idx:idx+2]
    return answer



# 다른 사람 풀이
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]
